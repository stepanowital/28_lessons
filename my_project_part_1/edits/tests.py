import inspect

from django.db import models
from django.db.models.fields import (
    BooleanField,
    CharField,
    DecimalField,
    SmallIntegerField,
    TextField,
)
from django.test import TestCase

from edits import models as student_models
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin, ResponseTestsMixin

LANGUAGES = [("ru", "Русский"), ("en", "Английский"), ("jp", "Японский")]

char_fields = {
    "title": {"max_length": 100},
    "language": {"max_length": 2, "choices": LANGUAGES},
    "start_point": {"max_length": 20},
    "end_point": {"max_length": 20},
}

text_fields = {"description": {}}

foreign_key_fields = {
    "city": {"on_delete": models.CASCADE, "model": student_models.City},
    "guide": {"on_delete": models.CASCADE, "model": student_models.Guide},
}

many_to_many_fields = {
    "attractions": {"model": student_models.Attractions},
}

decimal_fields = {"price_rur": {"max_digits": 10, "decimal_places": 2}}

boolean_fields = {
    "children_ok": {"default": True},
}

small_integer_fields = {"group_size": {}}

id_field = {"id": {"unique": True}}


def get_model_attributes(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result


class StoreClassTestCase(TestCase, ResponseTestsMixin, DataBaseTestsMixin):
    def test_store_has_expected_fields(self):
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
        expected_fields = get_model_attributes(
            char_fields,
            text_fields,
            foreign_key_fields,
            boolean_fields,
            many_to_many_fields,
            decimal_fields,
            id_field,
            small_integer_fields,
        )
        student_attrs_len = len(current_fields)
        expected_attrs_len = len(expected_fields)
        self.assertEqual(
            student_attrs_len,
            expected_attrs_len,
            (
                "%@ Проверьте, что добавили все необходимые поля в модель Tour."
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

        # Checking text_fields
        self.django_field_checker(current_fields, text_fields, TextField)

        # Checking decimal_fields
        self.django_field_checker(current_fields, decimal_fields, DecimalField)

        # Checking boolean_fields
        self.django_field_checker(current_fields, boolean_fields, BooleanField)

        # Checking small_integer_fields
        self.django_field_checker(
            current_fields, small_integer_fields, SmallIntegerField
        )

        # Checking city
        self.django_foreign_key_field_checker(
            current_fields["city"], foreign_key_fields["city"], models.ForeignKey
        )

        # Checking guide
        self.django_foreign_key_field_checker(
            current_fields["guide"], foreign_key_fields["guide"], models.ForeignKey
        )
        # Checking attractions
        self.django_foreign_key_field_checker(
            current_fields["attractions"],
            many_to_many_fields["attractions"],
            models.ManyToManyField,
        )
