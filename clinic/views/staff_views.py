from rest_framework import generics, permissions
from clinic import models
from clinic import serializers


# Контроллеры для CRUD операций model:clinic.models.MedStaffModel.
class StaffListView(generics.ListAPIView):
    """Контроллер для вывода списка сущностей models: clinic.model.MedStaffModel."""

    queryset = models.MedStaffModel.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class StaffCreateView(generics.CreateAPIView):
    """Контроллер для cсоздания сощности models: clinic.model.MedStaffModel."""

    queryset = models.MedStaffModel.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class StaffUpdateView(generics.UpdateAPIView):
    """Контроллер для изменения сущности models: clinic.model.MedStaffModel."""

    queryset = models.MedStaffModel.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class StaffRetrieveView(generics.RetrieveAPIView):
    """Контроллер для получения сущности models: clinic.model.MedStaffModel."""

    queryset = models.MedStaffModel.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class StaffDestroyView(generics.DestroyAPIView):
    """Контроллер для удаления models: clinic.model.MedStaffModel."""

    queryset = models.MedStaffModel.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
