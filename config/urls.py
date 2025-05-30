from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "appointment/",
        include("clinic.urls.urls_appointment", namespace="appointments"),
    ),
    path("staff/", include("clinic.urls.urls_staff", namespace="staff")),
    path("results/", include("clinic.urls.urls_results", namespace="results")),
    path("services/", include("clinic.urls.urls_services", namespace="services")),
    path("", include("users.urls", namespace="users")),
    path('', include('clinic.urls.urls_templates', namespace='main'))
]
