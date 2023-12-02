"""
test_forms.py
"""
from django.test import TestCase

from ..forms import NewUserForm


class TestBase(TestCase):
    """A test base class"""

    data: dict


class TestNewUserForm(TestBase):
    """Test new user form"""

    def test_form_fields(self):
        """Test fields defined in form"""
        form = NewUserForm()
        self.assertIn("username", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)
