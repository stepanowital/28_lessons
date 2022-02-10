
from django.urls import path

from first_opened.views import CityListView

urlpatterns = [
   path("pages/", CityListView.as_view()),
]
