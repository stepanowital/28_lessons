from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from along_neva_channels.models import Tour


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
                    "starts_at": tour.starts_at if tour.starts_at else "",
                    "ends_at": tour.ends_at if tour.ends_at else "",
                    "points": [{"name": point.name} for point in tour.points.all()],
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
                "starts_at": self.object.starts_at if self.object.starts_at else "",
                "ends_at": self.object.ends_at if self.object.ends_at else "",
                "points": list(self.object.points.all().values_list("name", flat=True)),
            }
        )
