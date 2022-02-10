from django.urls import path

from counting_rhyme.views import CountView

urlpatterns = [
    path("counting/", CountView.as_view()),
]
