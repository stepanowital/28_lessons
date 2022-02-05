from feedback.models import Review

from django.views.generic import CreateView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from feedback.models import Tour


@method_decorator(csrf_exempt, name="dispatch")
class ReviewCreateView(CreateView):
    model = Review
    fields = ["author", "tour", "content", "rate", "published_at", "is_published"]

    def post(self, request, *args, **kwargs):
        review_data = json.loads(request.body)

        review = Review()
        review.author = review_data["author"]
        review.content = review_data["content"]
        review.rate = review_data["rate"]
        review.is_published = review_data["is_published"]

        review.tour = get_object_or_404(Tour, pk=review_data["tour_id"])

        review.save()
        return JsonResponse(
            {
                "id": review.id,
                "author": review.author,
                "tour": review.tour_id,
                "content": review.content,
                "rate": review.rate,
                "published_at": review.published_at,
                "is_published": review.is_published,
            }
        )
