"""
test_models.py
"""
from django.test import TestCase
from tests import fixtures


class TestBase(TestCase):
    """Base test class containing setup for all budgets models"""

    user1: fixtures.User
    user2: fixtures.User

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user1 = fixtures.create_user()
        cls.user2 = fixtures.create_user()
