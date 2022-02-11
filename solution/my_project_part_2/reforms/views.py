from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from reforms.models import City
import json
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class CityUpdateView(UpdateView):
    model = City
    fields = ["name", "description"]

    def post(self, request, *args, **kwargs):
        city_data = json.loads(request.body)
        city, _ = City.objects.update_or_create(
            name=city_data["name"],
            defaults={
                "description": city_data["description"]
            }
        )
        city.save()
        return JsonResponse({
            "id": city.id,
            "name": city.name,
            "description": city.description,
        })
