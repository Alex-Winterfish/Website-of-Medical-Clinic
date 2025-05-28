from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    '''Сериалайзер для model:users.CustomUser.'''
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password",
            "country",
            "phone",
        ]
