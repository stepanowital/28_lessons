from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from moderation.models import Review


# TODO здесь необходимо реализовать CBV в соответствии с заданием
@method_decorator(csrf_exempt, name="dispatch")
class ReviewDeleteView(DeleteView):
    model = Review

    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
