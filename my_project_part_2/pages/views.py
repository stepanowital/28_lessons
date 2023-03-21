from django.core.paginator import Paginator
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

        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = int(request.GET.get("page", 1))

        page_obj = paginator.get_page(page_number)

        cities = []
        for city in page_obj:
            cities.append({
                "id": city.id,
                "name": city.name,
                "status": city.status,
            })

        response = {
            "total": paginator.count,
            "num_pages": paginator.num_pages,
            "items": cities
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})
