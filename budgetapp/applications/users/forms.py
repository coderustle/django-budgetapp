from django import forms
from django.contrib.auth.forms import UserCreationForm

from budgetapp.applications.users.models import User


class NewUserForm(UserCreationForm):
    """Form to register a new user"""

    class Meta(UserCreationForm.Meta):
        model = User
