from django.urls import path

from new_horizonts.views import CityCreateView

urlpatterns = [
    path("new_horizonts/", CityCreateView.as_view()),
]
