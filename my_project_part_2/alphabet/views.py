from django.views.generic import ListView
from alphabet.models import City
from django.http import JsonResponse


class CityListView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        cities = []
        for city in self.object_list:
            cities.append(
                {
                    "id": city.id,
                    "name": city.name,
                }
            )
        return JsonResponse(cities, safe=False)
