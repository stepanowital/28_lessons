import factory
from django.test import TestCase
from django.test.client import Client

from counting_rhyme import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.User


GET_CITIES = "/counting/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(20):
            CityFactory.create(name="test_city", status="closed")
        for _ in range(60):
            city = student_models.City.objects.get(id=5)
            UserFactory.create(city=city, username="testuser")
        self.student_app = Client()
        self.url = GET_CITIES
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(
                self.url, content_type="application/json"
            ),
            "expected": dict,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = (
            "cities",
            "users",
        )
        obj = response.json()
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            obj.get("cities") == 20,
            f"Проверьте что в ответе на GET-запрос по адресу {self.url} количество городов верное",
        )
        self.assertTrue(
            obj.get("users") == 60,
            f"Проверьте что в ответе на GET-запрос по адресу {self.url} количество пользователей верное",
        )
