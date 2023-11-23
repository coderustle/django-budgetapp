"""
urls.py
"""
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        view=views.login_request,
        name="login",
    ),
    path(
        "logout/",
        view=LogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        view=views.register_request,
        name="register",
    ),
]
