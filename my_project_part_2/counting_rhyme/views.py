from django.http import JsonResponse
from django.views import View


# TODO внесите необходимые изменения в код ниже
class CountView(View):
    def get(self):
        return JsonResponse({
            "cities": "",
            "users": "",
        })
