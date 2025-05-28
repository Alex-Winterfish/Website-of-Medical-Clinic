from rest_framework import generics, permissions
from clinic import models
from clinic import serializers

# Контроллеры для model:clinic.models.AppointmentModel.


class AppointmentListView(generics.ListAPIView):
    """Контроллер для получения списка model:clinic.models.AppointmentModel."""

    queryset = models.AppointmentModel.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class AppointmentCreateView(generics.CreateAPIView):
    """Контроллер для создания экземпляра model:clinic.models.AppointmentModel."""

    queryset = models.AppointmentModel.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class AppointmentRetrieveView(generics.RetrieveAPIView):
    """Контроллер для получения экземпляра model:clinic.models.AppointmentModel."""

    queryset = models.AppointmentModel
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class AppointmentUpdateView(generics.UpdateAPIView):
    """Контроллер для изменения экземпляра model:clinic.model.AppointmentModel."""

    queryset = models.AppointmentModel.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class AppointmentDestroyView(generics.DestroyAPIView):
    """Контроллер для удаления экземпляра model:clinic.models.AppointmentModel."""

    queryset = models.AppointmentModel.objects.all()
    serializer_class = serializers.AppointmentSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
