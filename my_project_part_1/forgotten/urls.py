# TODO настраиваем urls здесь
from django.urls import path

from forgotten import views

urlpatterns = [
    path('feedback-update/<int:pk>/', views.ReviewUpdateView.as_view())
]
