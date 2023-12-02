"""
urls.py
"""
from django.urls import path

from .views import home_page, index_page

app_name = "budget"


urlpatterns = [
    path("budget/", view=home_page, name="home"),
    path("", view=index_page, name="index"),
]
