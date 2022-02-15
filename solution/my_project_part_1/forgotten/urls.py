from django.urls import path

from forgotten.views import ReviewUpdateView

urlpatterns = [path("feedback-update/<int:pk>/", ReviewUpdateView.as_view())]
