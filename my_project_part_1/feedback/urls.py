# TODO настраиваем urls здесь
from django.urls import path

from feedback import views

urlpatterns = [
    path('feedback/', views.ReviewCreateView.as_view()),
]
