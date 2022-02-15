import factory
from django.test import TestCase
from django.test.client import Client

from forgotten import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin
import datetime


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.Review

    author = "Валерий Петров"
    content = "Очень понравился Осенний Питер"
    rate = 1
    is_published = True
    published_at = "2022-01-10 10:30:00"


class TourFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.Tour

    title = "Камчатские гейзеры"
    description = ("Прогулка по долине гейзеров Камчатки",)
    attractions = "Уникальные места Камчатке"


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City

    name = "test_city"


UPDATE_FEEDBACK = "/feedback-update/1/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(4):
            CityFactory.create()
        city_instance = student_models.City.objects.get(id=1)
        for _ in range(10):
            TourFactory.create(city_id=city_instance.id)
        tour_instance = student_models.Tour.objects.get(id=1)
        ReviewFactory.create(tour_id=tour_instance.id)
        review_for_create = {
            "tour_id": 4,
            "author": "wrong",
            "content": "new_content",
            "rate": 100,
            "is_published": False,
        }
        self.student_app = Client()
        self.url = UPDATE_FEEDBACK
        test_options = {
            "url": self.url,
            "method": "POST",
            "code": [200],
            "student_response": self.student_app.post(
                self.url, data=review_for_create, content_type="application/json"
            ),
            "expected": dict,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = (
            "id",
            "tour",
            "author",
            "content",
            "rate",
            "is_published",
            "published_at",
        )
        obj = response.json()
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на POST запрос по адресу {self.url} отсутствуют лишние поля",
        )
        new_values = {"content": "new_content", "rate": 100}
        old_values = {
            "id": 1,
            "author": "Валерий Петров",
            "tour": 1,
            "published_at": "2022-01-10T10:30:00",
            "is_published": True,
        }
        review_instance = student_models.Review.objects.get(id=1)
        for key, value in old_values.items():
            student_value = obj.get(key)
            self.assertTrue(
                value == student_value,
                f"Проверьте что при POST-запросе на адрес {self.url} поле {key} невозможно изменить",
            )
            if key == "tour":
                value = student_models.Tour.objects.get(id=1)
            if key == "published_at":
                value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            self.assertTrue(
                getattr(review_instance, key) == value,
                f"Проверьте что поле что при POST-запросе на адрес {self.url} поле {key} не изменилось в базе данных",
            )

        for key, value in new_values.items():
            student_value = obj.get(key)
            self.assertTrue(
                value == student_value,
                f"Проверьте что при POST-запросе на адрес {self.url} поле {key} изменяется",
            )
            self.assertTrue(
                getattr(review_instance, key) == value,
                f"Проверьте что поле что при POST-запросе на адрес {self.url} поле {key} не изменилось в базе данных",
            )
