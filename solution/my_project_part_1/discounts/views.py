from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from discounts.models import Discount


class DiscountListView(ListView):
    model = Discount

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for discount in self.object_list:
            response.append(
                {
                    "id": discount.id,
                    "tour": discount.tour_id,
                    "category": discount.category,
                    "discount": discount.discount,
                    "code": discount.code,
                    "starts_at": discount.starts_at if discount.starts_at else "",
                    "ends_at": discount.ends_at if discount.ends_at else "",
                }
            )

        return JsonResponse(response, safe=False)


class DiscountDetailView(DetailView):
    model = Discount

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse(
            {
                "id": self.object.id,
                "tour": self.object.tour_id,
                "category": self.object.category,
                "discount": self.object.discount,
                "code": self.object.code,
                "starts_at": self.object.starts_at if self.object.starts_at else "",
                "ends_at": self.object.ends_at if self.object.ends_at else "",
            }
        )
