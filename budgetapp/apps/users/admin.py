"""
admin.py
"""
from django.contrib import admin

from budgetapp.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
