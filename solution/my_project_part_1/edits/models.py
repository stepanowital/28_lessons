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
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    attractions = models.ManyToManyField(Attractions)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    price_rur = models.DecimalField(max_digits=10, decimal_places=2)
    start_point = models.CharField(max_length=20)
    end_point = models.CharField(max_length=20)
    children_ok = models.BooleanField(default=True)
    group_size = models.SmallIntegerField()
