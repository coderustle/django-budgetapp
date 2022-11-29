"""
test_views.py
"""

from django.test import TestCase
from django.urls import reverse
from django.conf import settings


from budgetapp.applications.users.models import User


class TestBase(TestCase):
    """A test base class containing a url and user attribute"""

    url: str
    user: User

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # Get rid of whitenoise "No directory at" warning,
        # as it's not helpful when running tests.
        settings.WHITENOISE_AUTOREFRESH = True


class TestLoginView(TestBase):
    """Test login page"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url = reverse("users:login")

    def test_login_page_template(self):
        """Test the template used by the login page"""
        response = self.client.get(self.url)
        expected = "registration/login.html"
        self.assertTemplateUsed(response=response, template_name=expected)


class TestRegisterView(TestBase):
    """Test register page"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url = reverse("users:register")

    def test_register_page_template(self):
        """Test the template used by the register page"""
        response = self.client.get(self.url)
        expected = "registration/register.html"
        self.assertTemplateUsed(response=response, template_name=expected)
