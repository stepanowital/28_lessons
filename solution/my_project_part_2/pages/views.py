from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView

from pages.models import City

# TODO максимальное число записей на одной странице не должно превышать 5 элементов

TOTAL_ON_PAGE = 5


class CityListView(ListView):
    model = City
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        cities = []
        for city in page_obj:
            cities.append(
                {
                    "id": city.id,
                    "name": city.name,
                    "status": city.status,
                }
            )
        response = {
            "items": cities,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False)
