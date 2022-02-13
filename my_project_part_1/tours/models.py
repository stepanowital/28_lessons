from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    attractions = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Review(models.Model):
    # TODO author  Имя пользователя  Короткий текст (максимальная длинна 20 символов)
    # TODO tour  Экскурсия Связь с моделью Tour (foreign key c каскадным удалением)
    # TODO content  Текст отзыва Длинный текст
    # TODO rate  Звездочки Маленькое целое число
    # TODO published_at  Время публикации  Дата и время
    # TODO is_published  Отзыв опубликован Логическое
    pass
