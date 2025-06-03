from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views import result_views

app_name = ClinicConfig.name

urlpatterns = [
    path("create/", result_views.ResultCreateView.as_view(), name="create_result"),
    path("delete/", result_views.ResultDeleteView.as_view(), name="delete_result"),
    path("list/", result_views.ResultListView.as_view(), name="results"),
    path(
        "detail/<int:pk>/",
        result_views.ResultDetailView.as_view(),
        name="detail_result",
    ),
    path("update/", result_views.ResultUpdateView.as_view(), name="update_result"),
]
