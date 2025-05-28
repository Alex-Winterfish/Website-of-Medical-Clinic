from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views import staff_views

app_name = ClinicConfig.name

urlpatterns = [
    path("create/", staff_views.StaffCreateView.as_view(), name="create_med_staff"),
    path("list/", staff_views.StaffListView.as_view(), name="med_personal"),
    path("update/", staff_views.StaffUpdateView.as_view(), name="update_med_staff"),
    path("delete/", staff_views.StaffDestroyView.as_view(), name="delete_med_staff"),
    path("detail/", staff_views.StaffRetrieveView.as_view(), name="detail_med_staff"),
]
