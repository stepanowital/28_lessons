import inspect

from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField
from django.test import TestCase

from tours import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin

char_fields = {
    "author": {"max_length": 20},
}

text_fields = {"content": {"max_length": 1000}}

foreign_key_fields = {
    "tour": {"on_delete": models.CASCADE, "model": student_models.Tour}
}

small_integer_fields = {"rate": {}}

boolean_fields = {
    "is_published": {"default": False},
}

date_time_fields = {"published_at": {"null": True, "blank": True}}

id_field = {"id": {"unique": True}}


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):
    def test_store_has_expected_fields(self):
        self.model = getattr(student_models, "Review", None)
        self.assertTrue(
            self.model, "%@Проверьте, что модель Review определена в модуле"
        )
        self.assertTrue(
            inspect.isclass(self.model), "Проверьте, что Review является классом"
        )
        self.assertTrue(
            issubclass(self.model, models.Model),
            "Проверьте, что класс Review правильно определен в модуле",
        )

        current_fields = {field.name: field for field in self.model._meta.fields}
        expected_fields = get_model_attributes(
            char_fields,
            text_fields,
            foreign_key_fields,
            boolean_fields,
            date_time_fields,
            id_field,
            small_integer_fields,
        )
        student_attrs_len = len(current_fields)
        expected_attrs_len = len(expected_fields)
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            (
                "%@ Проверьте, что добавили все необходимые поля в модель Review."
                f" Мы насчитали у Вас {student_attrs_len}, тогда как должно быть {expected_attrs_len}"
            ),
        )

        for field_name in expected_fields:
            self.assertIn(
                field_name,
                current_fields,
                f"Проверьте, что добавили в модель поле {field_name}",
            )

        # Checking char_fields
        self.django_field_checker(current_fields, char_fields, CharField)

        # Checking boolean_fields
        self.django_field_checker(current_fields, boolean_fields, BooleanField)

        # Checking datetime fields
        self.django_field_checker(current_fields, date_time_fields, DateTimeField)

        # Checking foreign_key_ tour
        self.django_foreign_key_field_checker(
            current_fields["tour"], foreign_key_fields["tour"], models.ForeignKey
        )
