"""
fixtures.py
"""
from typing import Optional

from django.contrib.auth import get_user_model
from faker import Faker

from budgetapp.apps.users.models import User


def create_user(
    username: str | None = None,
    password: str | None = None,
) -> User:
    """Create a new user in database"""
    fake = Faker("ro_Ro")
    user = get_user_model().objects.create(
        username=username if username else fake.user_name(),
        password=password if password else fake.text(max_nb_chars=10),
        email=fake.email(),
    )
    user.save()
    return user


def generate_user_data(
    email: Optional[str] = None,
    username: Optional[str] = None,
) -> dict:
    """Generate a dictionary with fake user data"""
    fake = Faker("ro_Ro")

    email = email if email else fake.email()
    username = username if username else fake.user_name()
    password = fake.text(max_nb_chars=10)

    data = {
        "username": username,
        "email": email,
        "password1": password,
        "password2": password,
    }
    return data
