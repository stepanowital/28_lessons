from django.contrib.auth.models import User
from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)


class Discount(models.Model):
    PROMO = "promo"
    CAMPAIGN = "campaign"
    DISCOUNT = "discount"
    CATEGORIES = [(PROMO, "Промокод"), (CAMPAIGN, "Акция"), (DISCOUNT, "Скидка")]

    category = models.CharField(max_length=8, choices=CATEGORIES, default=PROMO)
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
    )
    discount = models.PositiveSmallIntegerField(default=10)
    code = models.CharField(max_length=20, default="skypro")
    starts_at = models.DateTimeField(null=True)
    ends_at = models.DateTimeField(null=True)


# TODO после внесения соответствующих изменений в модель
# TODO Вам будет необходимо сформировать миграции (python3 manage.py makemigrations)
# TODO а также внести изменения в БД с помощью команды python3 manage.py migrate
# такие команды необходимо применять после каждого внесения изменений в модель
# кроме того, при дополнении таблицы полем, у которого нет значения по умолчанию
# или же значение которого не имеет параметра null = True При создании миграций
# Джанго поинтересуется каким значением необходимо создать такое поле.
# При подготовке проекта мы использовали команду loadall для загрузки фикстур
# в базу. (сами фикстуры содержатся в папке fixtures) Мы видим что мы загрузили
# две записи с ID = 1 и ID = 2.
# При выводе в терминале запроса от джанго "какое поле сделать по умолчанию"
# присвоим ему значение 1
# (выбираем опцию 1, нажимаем ввод и затем выбираем значение 1 и повторно нажимаем ввод)
# После этого все миграции должны быть корректно сформированы.
