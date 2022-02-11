from django.urls import path

from reforms.views import CityUpdateView

urlpatterns = [
    path("reforms/", CityUpdateView.as_view()),
]
