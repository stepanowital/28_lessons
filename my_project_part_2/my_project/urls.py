from django.contrib import admin
from django.urls import include, path

# TODO здесь подключаются urls Ваших приложений

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("new_horizonts.urls")),
    path("", include("reforms.urls")),
    path("", include("alphabet.urls")),
    path("", include("first_opened.urls")),
    path("", include("pages.urls")),
    path("", include("counting_rhyme.urls")),
    path("", include("users_geography.urls")),
]
