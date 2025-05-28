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


# Контроллеры для model:clinic.models.AppointmentModel.


class AppointmentLiatView(generics.ListAPIView):
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


# Контроллеры для model:clinic.models.ResultModel.


class ResultListView(generics.ListAPIView):
    """Контроллер для получения списка объектов model:clinic.models.ResultModel."""

    queryset = models.ResultModel.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class ResultCreateView(generics.CreateAPIView):
    """Контроллер для создания экземпляра model:clinic.models.ResultModel."""

    queryset = models.ResultModel.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class ResultRetrieveView(generics.RetrieveAPIView):
    """Контроллер для получения экземпляра model:clinic.models.ResultModel."""

    queryset = models.ResultModel.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class ResultUpdateView(generics.UpdateAPIView):
    """Контроллер для изменеия экземпляра model:clinic.models.ResultModel."""

    queryset = models.ResultModel.objects.all()
    serializers = serializers.ResultSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class ResultDestroyView(generics.DestroyAPIView):
    """Контроллер для удаления экземпляа model:clinic.models.ResultModel"""

    queryset = models.ResultModel.objects.all()
    serializer_class = serializers.ResultSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
