from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from along_neva_channels.models import Tour


# TODO Здесь необходимо реализовать CBV в соответствии со спецификацией
class TourListView(ListView):
    model = Tour

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for tour in self.object_list:
            response.append(
                {
                    "id": tour.id,
                    "name": tour.name,
                    "starts_at": tour.starts_at,
                    "ends_at": tour.ends_at,
                    "points": list(tour.points.all().values_list("name", flat=True))
                }
            )

        return JsonResponse(response, safe=False)


class TourDetailView(DetailView):
    model = Tour

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "starts_at": self.object.starts_at,
                "ends_at": self.object.ends_at,
                "points": list(self.object.points.all().values_list("name", flat=True))
            }
        )


class ReviewCreateView:
    pass