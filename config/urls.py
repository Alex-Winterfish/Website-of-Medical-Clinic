from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


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
    path('', include('clinic.urls.urls_templates', namespace='main')),
    path('', include('users.urls', namespace='client'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)