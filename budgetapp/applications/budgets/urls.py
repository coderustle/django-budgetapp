"""
urls.py
"""
from django.urls import path

from .views import home_page

app_name = "budgets"


urlpatterns = [
    path("", view=home_page, name="home"),
]