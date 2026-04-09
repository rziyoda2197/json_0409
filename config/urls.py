from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",   include("blog.urls")),
    # Brauzerda sinash uchun DRF login/logout
    path("api-auth/", include("rest_framework.urls")),
]