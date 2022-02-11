from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class CityUpdateView(UpdateView):
    # TODO напишите здесь Ваш код
    pass
