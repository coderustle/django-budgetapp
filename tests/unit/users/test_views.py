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


class TestLogin(TestBase):
    """Test login functionality"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url = reverse("users:login")

    def test_login_page_template(self):
        """Test the template used by the login page"""
        response = self.client.get(self.url)
        expected = "registration/login.html"
        self.assertTemplateUsed(response=response, template_name=expected)
