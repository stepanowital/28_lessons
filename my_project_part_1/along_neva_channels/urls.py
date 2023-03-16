# TODO настраиваем urls здесь
from django.urls import path

from along_neva_channels import views

urlpatterns = [
    path('neva_tours/', views.TourListView.as_view()),
    path('neva_tours/<int:pk>', views.TourDetailView.as_view()),
]
