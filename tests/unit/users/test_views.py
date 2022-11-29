"""
test_views.py
"""

from django.test import TestCase
from django.urls import reverse
from django.conf import settings


from budgetapp.applications.users.models import User
from tests import fixtures


class TestBase(TestCase):
    """A test base class containing a url and user attribute"""

    url: str
    user: User


class TestLoginView(TestBase):
    """Test login page"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url = reverse("users:login")
        cls.user = fixtures.generate_db_user()

    def test_login_page_template(self):
        """Test the template used by the login page"""
        response = self.client.get(self.url)
        expected = "registration/login.html"
        self.assertTemplateUsed(response=response, template_name=expected)

    def test_login_user_form(self):
        """Test login user form"""
        self.user.set_password("test1234")
        self.user.save()

        data = {"username": self.user.username, "password": "test1234"}

        response = self.client.post(self.url, data=data)
        expected_url = "/budgets/"

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, expected_url)

    def test_login_user_form_bad_wrong_password(self):
        """Test login user form with wrong password"""
        data = {"username": self.user.username, "password": "wrong"}

        response = self.client.post(self.url, data=data)
        expected_url = "/users/login/"

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, expected_url)


class TestLogoutView(TestBase):
    """Test logout functionality"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url = reverse("users:logout")
        cls.user = fixtures.generate_db_user()

    def test_logout_page_redirection(self):
        """Test if the user is redirected to login page"""

        # login the user
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        expected_url = "/users/login/"

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, expected_url)

    def test_logout_page_redirection_unauthenticated_user(self):
        """Test trying to access the logout view for unauthenticated user"""
        response = self.client.get(self.url)
        expected_url = "/users/login/"

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, expected_url)


class TestRegisterView(TestBase):
    """Test register page"""

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.url = reverse("users:register")

    def test_register_page_template(self):
        """Test the template used by the register page"""
        response = self.client.get(self.url)
        expected = "registration/register.html"
        self.assertTemplateUsed(response=response, template_name=expected)

    def test_register_new_user(self):
        """Test register new user. The user is logged in and redirected"""

        data = fixtures.generate_data_user()
        response = self.client.post(self.url, data=data)
        expected_url = "/budgets/"

        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, expected_url)
