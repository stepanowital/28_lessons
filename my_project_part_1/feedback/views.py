import json

from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from feedback.models import Review


# TODO здесь необходимо реализовать CBV в соответствии с заданием
@method_decorator(csrf_exempt, name="dispatch")
class ReviewCreateView(CreateView):
    model = Review
    fields = ["author", "tour", "content", "rate", "published_at", "is_published"]

    def post(self, request, *args, **kwargs):
        review_data = json.loads(request.body)

        review = Review.objects.create(
            tour_id=review_data["tour_id"],
            author=review_data["author"],
            content=review_data["content"],
            rate=review_data["rate"],
            is_published=review_data["is_published"],
        )

        return JsonResponse(
            {
                "id": review.id,
                "author": review.author,
                "tour": review.tour_id,
                "content": review.content,
                "rate": review.rate,
                "published_at": review.published_at,
                "is_published": review.is_published
            }
        )
