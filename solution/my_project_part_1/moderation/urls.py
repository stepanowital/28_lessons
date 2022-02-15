from django.urls import path

from moderation.views import ReviewDeleteView

urlpatterns = [path("feedback-delete/<int:pk>/", ReviewDeleteView.as_view())]
