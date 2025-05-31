from clinic.apps import ClinicConfig
from django.urls import path
from clinic.views.templates_views import MainPageView, CompanyInfo

app_name = ClinicConfig.name

urlpatterns = [
    path("main/", MainPageView.as_view(), name="main"),
    path('company_page/', CompanyInfo.as_view(), name='company_page')
]