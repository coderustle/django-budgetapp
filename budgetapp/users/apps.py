"""
apps.py
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Config for users app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "budgetapp.users"
