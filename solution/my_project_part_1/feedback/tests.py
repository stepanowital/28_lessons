import factory
from django.test import TestCase
from django.test.client import Client

from feedback import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


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


CREATE_FEEDBACK = "/feedback/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(4):
            CityFactory.create()
        city_instance = student_models.City.objects.get(id=1)
        for _ in range(10):
            TourFactory.create(city_id=city_instance.id)
        review_for_create = {
            "tour_id": 8,
            "author": "test_author",
            "content": "Мне понравилось! Отличный тур",
            "rate": 5,
            "is_published": True,
        }
        self.student_app = Client()
        self.url = CREATE_FEEDBACK
        test_options = {
            "url": self.url,
            "method": "POST",
            "code": [200, 201],
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

        # Проверяем, сохранены ли данные в БД
        objects_count = student_models.Review.objects.all().count()
        self.assertTrue(
            objects_count == 1,
            f"Проверьте, сохраняется ли информация в базе данных при POST-запросе на адрес {self.url}",
        )
