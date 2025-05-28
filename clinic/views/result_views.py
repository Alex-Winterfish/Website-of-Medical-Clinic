from rest_framework import generics, permissions
from clinic import models
from clinic import serializers

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
