import factory
from django.test import TestCase
from django.test.client import Client

from moderation import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


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


DELETE_FEEDBACK = "/feedback-delete/1/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(4):
            CityFactory.create()
        city_instance = student_models.City.objects.get(id=1)
        for _ in range(10):
            TourFactory.create(city_id=city_instance.id)
        tour_instance = student_models.Tour.objects.get(id=1)
        for _ in range(10):
            ReviewFactory.create(tour_id=tour_instance.id)

        self.student_app = Client()
        self.url = DELETE_FEEDBACK
        test_options = {
            "url": self.url,
            "method": "DELETE",
            "code": [302, 200, 204],
            "student_response": self.student_app.post(self.url),
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        count = student_models.Review.objects.all().count()
