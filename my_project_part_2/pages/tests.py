import factory
from django.test import TestCase
from django.test.client import Client

from pages import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City


GET_CITIES = "/pages/?page=2"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        for _ in range(50):
            CityFactory.create(name="bca_test", status="closed")
            CityFactory.create(name="abc_test", status="closed")
            CityFactory.create(name="zyx_test", status="open")
            CityFactory.create(name="nmk_test", status="open")
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
            "items",
            "num_pages",
            "total",
        )
        obj = response.json()
        for attribute in expected_attributes:
            self.assertIn(
                attribute,
                obj,
                f"Проверьте, что ответ на GET-запрос по адресу {self.url} "
                f"возвращается словарь, который содержат в себе поле {attribute}",
            )
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на POST запрос по адресу {self.url} отсутствуют лишние поля",
        )
        obj = response.json().get("items")
        self.assertTrue(
            len(obj) == 5, "Проверьте что на странице содержится максимум 5 объектов"
        )
        count_obj = response.json().get("total")
        self.assertTrue(
            count_obj == 200,
            "Проверьте, что значение total содержит верное значение (общее количество объектов)",
        )
        num_pages = response.json().get("num_pages")
        self.assertTrue(
            num_pages == 40,
            "Проверьте, что значение num_pages содержит верное значение (общее количество страниц)",
        )
        obj = response.json().get("items")[0]
        expected_attributes = (
            "id",
            "name",
            "status",
        )
        self.check_expected_attributes(obj, expected_attributes)
