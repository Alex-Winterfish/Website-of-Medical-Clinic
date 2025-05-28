from rest_framework import generics, permissions
from clinic import models
from clinic import serializers

# Контроллеры для CRUD операций model:clinic.models.MedServiceModel.


class ServiceListView(generics.ListAPIView):
    """Контроллер для вывода списка model:clinic.models.MedServiceModel."""

    queryset = models.MedServiceModel.objects.all()
    serializer_class = serializers.ServiceSerailizer
    permission_classes = [
        permissions.AllowAny,
    ]


class ServiceCreateView(generics.CreateAPIView):
    """Контроллер для создания model:clinic.models.MedServiceModel."""

    queryset = models.MedServiceModel.objects.all()
    serializer_class = serializers.ServiceSerailizer
    permission_classes = [
        permissions.AllowAny,
    ]


class ServiceRetrieveView(generics.RetrieveAPIView):
    """Контроллер для получения model:clinic.models.MedServiceModel."""

    queryset = models.MedServiceModel.objects.all()
    serializer_class = serializers.ServiceSerailizer
    permission_classes = [
        permissions.AllowAny,
    ]


class ServiceUpdateView(generics.UpdateAPIView):
    """Контроллер для получения model:clinic.models.MedServiceModel."""

    queryset = models.MedServiceModel.objects.all()
    serializer_class = serializers.ServiceSerailizer
    permission_classes = [
        permissions.AllowAny,
    ]


class ServiceDestroyView(generics.DestroyAPIView):
    """Контроллер для удаления экземпляра model:clinic.models.MedService."""

    queryset = models.MedServiceModel.objects.all()
    serializer_class = serializers.ServiceSerailizer
    permission_classes = [
        permissions.AllowAny,
    ]
