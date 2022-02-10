from django.urls import path

from first_opened.views import CityListView

urlpatterns = [
    path("first_opened/", CityListView.as_view()),
]
