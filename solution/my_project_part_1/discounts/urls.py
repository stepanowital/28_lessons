from django.urls import path

from discounts.views import DiscountDetailView, DiscountListView

urlpatterns = [
    path("discount/", DiscountListView.as_view()),
    path("discount/<int:pk>", DiscountDetailView.as_view()),
]
