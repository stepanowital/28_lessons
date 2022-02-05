from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    attractions = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Review(models.Model):
    author = models.CharField(max_length=20)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    rate = models.SmallIntegerField()
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
