from django.db import models


class Point(models.Model):
    name = models.CharField(max_length=20)


class Tour(models.Model):
    name = models.CharField(max_length=20)
    starts_at = models.DateTimeField(null=True)
    ends_at = models.DateTimeField(null=True)
    points = models.ManyToManyField(Point)
