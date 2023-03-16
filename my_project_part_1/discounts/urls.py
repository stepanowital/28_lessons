# TODO настраиваем urls здесь
from django.urls import path

from discounts import views

urlpatterns = [
    path('discount/', views.DiscountListView.as_view()),
    path('discount/<int:pk>', views.DiscountDetailView.as_view()),
]
