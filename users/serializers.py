# -*- coding: UTF-8 -*-
from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для model:users.CustomUser."""

    class Meta:
        model = CustomUser
        fields = [
            'last_name',
            'first_name',
            'patronymic',
            "country",
            'email',
            "phone",
        ]
