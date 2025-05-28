from django.contrib import admin

from clinic import models


@admin.register(models.MedStaffModel)
class StaffAdmin(admin.ModelAdmin):
    """Аднинка для model:clinic.models.MedStaffModel."""

    list_display = ["name", "title", "speciality"]
    list_filter = ["name"]
    search_help_text = "name"


@admin.register(models.MedServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    """Админка для model:clinic.models.MedServiceModel."""

    list_display = ["name", "description"]
    list_filter = ["name"]
    search_help_text = "name"


@admin.register(models.AppointmentModel)
class AppointmentAdmin(admin.ModelAdmin):
    """Админка для model:clinic.models.AppointmentModel"""

    list_display = ["ap_date", "med_serv", "med_spec", "patient"]
    list_filter = ["patient", "ap_date"]
    search_help_text = "patient"


@admin.register(models.ResultModel)
class ResultAdmin(admin.ModelAdmin):
    """Админгка для model:clinic.models.ResultModel."""

    list_display = ["result_date", "appointment", "result", "patient"]
    list_filter = ["patient"]
    search_help_text = "patient"
