from django.urls import path

from along_neva_channels.views import TourListView, TourDetailView

urlpatterns = [
    path("neva_tours/", TourListView.as_view()),
    path("neva_tours/<int:pk>/", TourDetailView.as_view()),
]
