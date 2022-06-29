"""
Users Application models.
"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model which extends the Django base user"""

    class Meta:
        db_table = "auth_user"
