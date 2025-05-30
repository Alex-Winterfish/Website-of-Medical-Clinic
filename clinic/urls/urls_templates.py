from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views.templates_views import MainPageView

app_name = ClinicConfig.name

urlpatterns = [
    path("main/", MainPageView.as_view(), name="main"),]