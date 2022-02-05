from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView


# TODO здесь необходимо реализовать CBV в соответствии с заданием
@method_decorator(csrf_exempt, name="dispatch")
class ReviewDeleteView(DeleteView):
    pass
