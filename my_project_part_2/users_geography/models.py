from django.db import models


class City(models.Model):
    STATUSES = [("open", "Open"), ("closed", "Closed")]

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=6, choices=STATUSES, default="open")

    class Meta:
        ordering = ["name"]


class User(models.Model):
    username = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
