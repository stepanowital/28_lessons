import inspect

import factory
from django.db import models
from django.db.migrations.recorder import MigrationRecorder
from django.db.models.fields import CharField, DateTimeField
from django.test import TestCase
from django.test.client import Client

from along_neva_channels import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class TourFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.Tour

    name = "promo"
    starts_at = "2021-05-05 12:00:30"
    ends_at = "2022-08-20 12:00:30"

    @factory.post_generation
    def points(self, create, extracted):
        if not create:
            return

        if extracted:
            for point in extracted:
                self.points.add(point)


class PointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = student_models.Point

    name = "test_point"


TOURS_LIST = "/neva_tours/"
GET_TOUR = "/neva_tours/4/"


def get_test_queryset(url):
    if url == GET_TOUR:
        return student_models.Tour.objects.get(id=3)
    if url == TOURS_LIST:
        return student_models.Tour.objects.all()


class ModelTestCase(TestCase, DataBaseTestsMixin, ResponseTestsMixin):
    @classmethod
    def setUpClass(cls):
        super(ModelTestCase, cls).setUpClass()

        cls.char_fields = {"name": {}}

        cls.datetime_fields = {"starts_at": {"null": True}, "ends_at": {"null": True}}

        cls.id_field = {"id": {"unique": True}}

        cls.many_to_many_fields = {
            "points": {"model": student_models.Point},
        }

        cls.expected_fields = get_model_attributes(
            cls.char_fields,
            cls.datetime_fields,
            cls.many_to_many_fields,
            cls.id_field,
        )

    def discount_model_is_correct(self):
        model_name = "Tour"
        self.model = getattr(student_models, model_name, None)
        self.assertTrue(
            self.model, f"%@Проверьте, что модель {model_name} определена в модуле"
        )
        self.assertTrue(
            inspect.isclass(self.model), f"Проверьте, что {model_name} является классом"
        )
        self.assertTrue(
            issubclass(self.model, models.Model),
            f"Проверьте, что класс {model_name} правильно определен в модуле",
        )
        current_fields = {field.name: field for field in self.model._meta.get_fields()}
        student_attrs_len = len(current_fields)
        expected_attrs_len = len(self.expected_fields)
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            (
                f"%@ Проверьте, что добавили все необходимые поля в модель {model_name}."
                f" Мы насчитали у Вас {student_attrs_len}, тогда как должно быть {expected_attrs_len}"
            ),
        )
        for field_name in self.expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}",
            )

        self.django_foreign_key_field_checker(
            current_fields["points"],
            self.many_to_many_fields["points"],
            models.ManyToManyField,
        )

        # Checking char_fields
        self.django_field_checker(current_fields, self.char_fields, CharField)

        # Checking datetime_fields
        self.django_field_checker(current_fields, self.datetime_fields, DateTimeField)

    def data_base_has_new_migrations(self):
        discounts_count = MigrationRecorder.Migration.objects.filter(
            app="along_neva_channels"
        ).count()
        self.assertTrue(
            discounts_count > 1,
            "Убедитесь, что выполнили команды makemigrations для создания новых миграций и migrate чтобы применить изменения к базе данных",
        )

    def urls_returns_correct_answers(self):
        for _ in range(4):
            PointFactory.create()
        points_instances = student_models.Point.objects.all()
        for _ in range(10):
            TourFactory.create(points=(point for point in points_instances))
        self.student_app = Client()
        self.url = GET_TOUR
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(self.url),
            "expected": dict,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = ("id", "points", "name", "starts_at", "ends_at")
        obj = response.json()
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на GET запрос по адресу {self.url} отсутствуют лишние поля",
        )
        points = obj.get("points")
        self.assertIsInstance(
            points,
            list,
            f"Проверьте, в ответе на GET запрос по адресу {self.url} поле points является списком",
        )
        for point in points:
            self.assertTrue(
                point == "test_point",
                f"Проверьте, что в ответе на GET запрос по адресу {self.url} список points содержит верные значения",
            )

        self.url = TOURS_LIST
        test_options = {
            "url": self.url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(self.url),
            "expected": list,
            "django_mode": True,
        }
        response = self.check_status_code_jsonify_and_expected(**test_options)
        expected_attributes = ("id", "points", "name", "starts_at", "ends_at")
        obj = response.json()[0]
        self.check_expected_attributes(obj, expected_attributes)
        self.assertTrue(
            len(obj.keys()) == len(expected_attributes),
            f"Проверьте, что в ответе на GET запрос по адресу {self.url} отсутствуют лишние поля",
        )
        points = obj.get("points")
        self.assertIsInstance(
            points,
            list,
            f"Проверьте, в ответе на GET запрос по адресу {self.url} поле points является списком",
        )
        for point in points:
            self.assertTrue(
                point == "test_point",
                f"Проверьте, что в ответе на GET запрос по адресу {self.url} список points содержит верные значения",
            )

    def test_run_tests_in_order(self):
        self.discount_model_is_correct()  # checks model is correct
        self.data_base_has_new_migrations()
        self.urls_returns_correct_answers()
