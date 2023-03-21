from django.db.models import Count
from django.http import JsonResponse
from django.views import View

from counting_rhyme.models import City, User


# TODO внесите необходимые изменения в код ниже
class CountView(View):
    def get(self, request):
        cities = City.objects.aggregate(total=Count("pk"))
        users = User.objects.aggregate(total=Count("pk"))
        return JsonResponse(
            {
                "cities": cities["total"],
                "users": users["total"],
            }
        )

