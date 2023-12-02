"""
test_models.py
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker


class TestBase(TestCase):
    """Base test class containing setup for all users models"""

    fake: Faker
    email: str
    username: str

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.fake = Faker("ro_Ro")
        cls.username = cls.fake.user_name()
        cls.email = cls.fake.email()


class TestUserModel(TestBase):
    """Contains the tests for User model"""

    def test_create_new_user(self):
        """Test creating new user"""
        user = get_user_model().objects.create(
            username=self.username, email=self.email
        )

        self.assertEqual(user.email, self.email)
        self.assertEqual(user.username, self.username)

    def test_create_new_super_user(self):
        """Test creating a superuser"""
        superuser = get_user_model().objects.create_superuser(
            username=self.username,
            email=self.email,
            password="password",
        )

        self.assertEqual(superuser.username, self.username)
        self.assertEqual(superuser.email, self.email)
