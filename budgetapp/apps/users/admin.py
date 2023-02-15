"""
admin.py
"""
from django.contrib import admin

from budgetapp.applications.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
