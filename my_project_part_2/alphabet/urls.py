from django.urls import path

from alphabet.views import CityListView

urlpatterns = [
    path("alphabet/", CityListView.as_view()),
]
