from django import forms
from django.contrib.auth.forms import UserCreationForm

from budgetapp.apps.users.models import User


class NewUserForm(UserCreationForm):
    """Form to register a new user"""

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
