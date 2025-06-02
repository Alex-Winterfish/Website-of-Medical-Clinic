from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="clinic:main"), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('user_page/', views.UserPageView.as_view(), name='user_page'),
    path('feedback/', views.FeedBackCreateView.as_view(), name='feedback')
]