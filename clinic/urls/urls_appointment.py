from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views import appointment_views

app_name = ClinicConfig.name

urlpatterns = [
    path(
        "create/",
        appointment_views.AppointmentCreateView.as_view(),
        name="create_appointment",
    ),
    path(
        "delete/",
        appointment_views.AppointmentDestroyView.as_view(),
        name="delete_appointment",
    ),
    path("list/", appointment_views.AppointmentListView.as_view(), name="appointments"),
    path(
        "detail/",
        appointment_views.AppointmentRetrieveView.as_view(),
        name="detail_appointment",
    ),
    path(
        "update/",
        appointment_views.AppointmentUpdateView.as_view(),
        name="update_appointment",
    ),
]
