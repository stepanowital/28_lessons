from django.http import JsonResponse
from django.views.generic import ListView

from first_opened.models import City


import json

from django.http import JsonResponse
from django.views.generic import ListView

from first_opened.models import City


# TODO вам предстоит переработать этот CBV
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
