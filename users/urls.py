from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterUserView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    # path("email_confirm/<str:token>/", email_verification, name="email_confirm"),
    # path('reset_password/', ChangePasswordView.as_view(), name='reset_password')
]
