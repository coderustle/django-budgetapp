"""
fixtures.py
"""
from faker import Faker
from django.contrib.auth import get_user_model

from budgetapp.applications.users.models import User


def generate_db_user() -> User:
    """Create a new user in database"""
    fake = Faker("ro_Ro")
    user = get_user_model().objects.create(
        username=fake.user_name(),
        password=fake.text(max_nb_chars=10),
        email=fake.email(),
    )
    user.save()
    return user
