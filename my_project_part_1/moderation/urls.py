# TODO настраиваем urls здесь
from django.urls import path

from moderation import views

urlpatterns = [
    path('feedback-delete/<int:pk>', views.ReviewDeleteView.as_view())
]
