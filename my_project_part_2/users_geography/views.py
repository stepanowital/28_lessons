from django.views.generic import ListView

from users_geography.models import City


# TODO внесите необходимые изменения в код ниже
class CityRateView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        pass
