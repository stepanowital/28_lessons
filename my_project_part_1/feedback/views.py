from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# TODO здесь необходимо реализовать CBV в соответствии с заданием
@method_decorator(csrf_exempt, name="dispatch")
class ReviewCreateView(CreateView):
    pass
