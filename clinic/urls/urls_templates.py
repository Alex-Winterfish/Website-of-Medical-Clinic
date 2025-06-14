from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views.templates_views import MainPageView, ContactsView, SuccessResulView

app_name = ClinicConfig.name

urlpatterns = [
    path("main_page/", MainPageView.as_view(), name="main"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("result_created/", SuccessResulView.as_view(), name="result_created"),
]
