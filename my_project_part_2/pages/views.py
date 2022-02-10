from django.http import JsonResponse
from django.views.generic import ListView

from pages.models import City

# TODO максимальное число записей на одной странице не должно превышать 5 элементов
TOTAL_ON_PAGE = 5


# TODO внесите необходимые изменения в код ниже
class CityListView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cities = []
        for city in self.object_list:
            cities.append({
                "id": city.id,
                "name": city.name,
                "status": city.status,
            })

        return JsonResponse(cities, safe=False)
