import factory
from django.test import TestCase
from django.test.client import Client

from first_opened import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City


GET_CITIES = "/first_opened/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
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
            "expected": list,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = (
            "id",
            "name",
            "status",
        )
        obj = response.json()[0]
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на POST запрос по адресу {self.url} отсутствуют лишние поля",
        )
        for obj, start_key in zip(response.json(), ["n", "z", "a", "b"]):
            self.assertTrue(
                obj.get("name")[0] == start_key,
                f"Проверьте, что при GET-запросе на адрес {self.url} возвращаемый список отсортирован по алфавиту",
            )
