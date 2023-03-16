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
    # ODO дополните модель следующими данными:
    # ODO guide Гид Связь с моделью Guide (foreign key с каскадным удалением)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    # ODO attractions Достопримечательности M2M поле
    attractions = models.ManyToManyField(Attractions)
    # ODO language  Язык, например ru / en / jp  Короткий текст (2) (выбор)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='ru')
    # ODO price_rur Цена в рублях, например 1200 Десятичное число
    price_rur = models.DecimalField(decimal_places=2, max_digits=10)
    # ODO start_point Точка начала  Короткий текст (20)
    start_point = models.CharField(max_length=20)
    # ODO end_point Точка завершения  Короткий текст (20)
    end_point = models.CharField(max_length=20)
    # ODO children_ok Можно детям или с детьми  Логическое, по умолчанию true
    children_ok = models.BooleanField(default=True)
    # TODO group_size  Размер группы Маленькое число
    group_size = models.SmallIntegerField()
