from django.urls import path

from users_geography.views import CityRateView

urlpatterns = [
    path("users_geography/", CityRateView.as_view()),
]
