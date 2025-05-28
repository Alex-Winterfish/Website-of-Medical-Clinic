from rest_framework import serializers
from clinic import models


class StaffSerializer(serializers.ModelSerializer):
    """Сериалайзер для model:clinic.models.MedStaffModel."""

    class Meta:
        model = models.MedStaffModel
        fields = ["name", "title", "speciality"]


class ServiceSerailizer(serializers.ModelSerializer):
    """Сериалайзер для model:clinic.models.MedServiceModel."""

    class Meta:
        model = models.MedServiceModel
        fields = ["name", "description"]


class AppointmentSerializer(serializers.ModelSerializer):
    """Сериалайзер для model:clinic.models.AppointmentModel."""

    class Meta:
        model = models.AppointmentModel
        fields = ["ap_date", "med_serv", "med_spec", "patient"]


class ResultSerializer(serializers.ModelSerializer):
    """Сериалайзер для model:clinic.models.ResultModel."""

    class Meta:
        model = models.ResultModel
        fields = ["result_date", "appointment", "result", "patient"]
