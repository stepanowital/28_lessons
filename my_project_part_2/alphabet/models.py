from django.db import models


# TODO добавьте необходимые опции для модели здесь
class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]
