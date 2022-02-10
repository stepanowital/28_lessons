from django.urls import path

from pages.views import CityListView

urlpatterns = [
    path("pages/", CityListView.as_view()),
]
