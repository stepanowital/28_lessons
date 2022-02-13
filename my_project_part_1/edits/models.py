from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Guide(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    tours_count = models.SmallIntegerField()
    is_pro = models.BooleanField(default=False)


class Attractions(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    coordinates = models.CharField(max_length=20)


class Tour(models.Model):
    LANGUAGES = [("ru", "Русский"), ("en", "Английский"), ("jp", "Японский")]

    title = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # TODO дополните модель следующими данными:
    # TODO guide Гид Связь с моделью Guide (foreign key с каскадным удалением)
    # TODO attractions Достопримечательности M2M поле
    # TODO language  Язык, например ru / en / jp  Короткий текст (2) (выбор)
    # TODO price_rur Цена в рублях, например 1200 Десятичное число
    # TODO start_point Точка начала  Короткий текст (20)
    # TODO end_point Точка завершения  Короткий текст (20)
    # TODO children_ok Можно детям или с детьми  Логическое, по умолчанию true
    # TODO group_size  Размер группы Маленькое число
