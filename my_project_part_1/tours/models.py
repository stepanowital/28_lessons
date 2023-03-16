from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    attractions = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Review(models.Model):
    # ODO author  Имя пользователя  Короткий текст (максимальная длинна 20 символов)
    author = models.CharField(max_length=20)
    # ODO tour  Экскурсия Связь с моделью Tour (foreign key c каскадным удалением)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    # ODO content  Текст отзыва Длинный текст
    content = models.TextField(max_length=1000)
    # ODO rate  Звездочки Маленькое целое число
    rate = models.SmallIntegerField()
    # ODO published_at  Время публикации  Дата и время
    published_at = models.DateTimeField(null=True, blank=True)
    # ODO is_published  Отзыв опубликован Логическое
    is_published = models.BooleanField(default=False)
