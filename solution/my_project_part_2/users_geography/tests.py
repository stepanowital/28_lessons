import factory
from django.test import TestCase
from django.test.client import Client

from users_geography import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.User


GET_CITIES = "/users_geography/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(5):
            CityFactory.create(name="test_city", status="closed")
        for _ in range(10):
            city = student_models.City.objects.get(id=1)
            UserFactory.create(city=city, username="testuser")
        for _ in range(10):
            city = student_models.City.objects.get(id=2)
            UserFactory.create(city=city, username="testuser")
        for _ in range(10):
            city = student_models.City.objects.get(id=3)
            UserFactory.create(city=city, username="testuser")
        for _ in range(10):
            city = student_models.City.objects.get(id=4)
            UserFactory.create(city=city, username="testuser")
        for _ in range(40):
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
            "expected": list,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = (
            "id",
            "name",
            "status",
            "users",
            "users_percent",
        )
        instance = None

        for obj in response.json():
            if obj.get("id") == 5:
                instance = obj
        self.check_expected_attributes(instance, expected_attributes)
        self.assertTrue(
            instance.get("users") == 40,
            f"Проверьте что в ответе на GET-запрос по адресу {self.url} количество пользователей верное",
        )
        self.assertTrue(
            instance.get("users_percent") == 0.5,
            f"Проверьте что в ответе на GET-запрос по адресу {self.url} правильно рассчитан процент пользователей",
        )
