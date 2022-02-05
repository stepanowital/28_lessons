from django.urls import path

from feedback.views import ReviewCreateView

urlpatterns = [path("feedback/", ReviewCreateView.as_view())]
