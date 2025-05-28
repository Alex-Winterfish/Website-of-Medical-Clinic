from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views import service_views

app_name = ClinicConfig.name

urlpatterns = [
    path(
        "create/", service_views.ServiceCreateView.as_view(), name="create_med_service"
    ),
    path(
        "delete/", service_views.ServiceDestroyView.as_view(), name="delete_med_service"
    ),
    path("list/", service_views.ServiceListView.as_view(), name="med_services"),
    path("detail/", service_views.ServiceRetrieveView.as_view(), name="detail_service"),
    path("update/", service_views.ServiceUpdateView.as_view(), name="update_service"),
]
