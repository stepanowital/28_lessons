import factory
from django.test import TestCase
from django.test.client import Client

from new_horizonts import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin
from new_horizonts import views
import inspect
import re


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.City

    name = "test_city"


CREATE_FEEDBACK = "/new_horizonts/"


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    def test_urls_returns_correct_answers(self):
        CityFactory.create()
        city_json = {"name": "test_city"}
        self.student_app = Client()
        self.url = CREATE_FEEDBACK
        test_options = {
            "url": self.url,
            "method": "POST",
            "code": [200, 201],
            "student_response": self.student_app.post(
                self.url, data=city_json, content_type="application/json"
            ),
            "expected": dict,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = ("id", "name")
        obj = response.json()
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на POST запрос по адресу {self.url} отсутствуют лишние поля",
        )

        # Проверяем, не записался ли в БД новый объект
        objects_count = student_models.City.objects.all().count()
        self.assertTrue(
            objects_count == 1,
            f"Проверьте, что при POST-запросе на адрес {self.url} в случае если город существует в базе не создается ли еще один который его дублирует",
        )
        test_options["student_response"] = self.student_app.post(
            self.url, data={"name": "new_city"}, content_type="application/json"
        )
        self.check_status_code_jsonify_and_expected(**test_options)
        objects_count = student_models.City.objects.all().count()
        self.assertTrue(
            objects_count == 2,
            f"Проверьте, что при POST-запросе на адрес {self.url} в случае если города еще нет в базе существует в базе, то создаётся новый объект",
        )

    def test_view_class_exists(self):
        view = getattr(views, "CityCreateView")
        self.assertTrue(
            view,
            "Проверьте что класс CityCreateView находится в модуле views, он необходим нам, для корректной проверки",
        )
        view_code = inspect.getsource(views.CityCreateView)
        wrong_code = ["try", "except"]
        for word in wrong_code:
            self.assertNotIn(
                word,
                view_code,
                "Пожалуйста, не используйте в задании конструкции try-except",
            )
        self.assertIn(
            "get_or_create",
            view_code,
            "Попробуйте воспользоваться функцией get_or_create",
        )
