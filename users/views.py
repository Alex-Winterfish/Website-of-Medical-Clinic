from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from users import models
from users import serializers
class CustomUserViewSet(viewsets.ModelViewSet):
    '''ViewSet для model:users.models.CustomUser'''
    queryset = models.CustomUser.objects.all()
    serializer_class = models.CustomUserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class MyTokenObtainPairView(TokenObtainPairView):
    """Аутентификация пользователя"""

    permission_classes = (permissions.AllowAny,)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["email"] = user.email

        return token
