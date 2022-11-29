"""
test_login.py
"""
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

from tests.functional import pom


class TestLiveServerBase(StaticLiveServerTestCase):
    """Base live server class"""

    page: pom.BasePage

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # Get rid of whitenoise "No directory at" warning,
        # as it's not helpful when running tests.
        settings.WHITENOISE_AUTOREFRESH = True


class TestLoginPage(TestLiveServerBase):
    """Test login functionallity"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        geckodriver = GeckoDriverManager().install()
        browser = Firefox(executable_path=geckodriver)
        cls.page = pom.LoginPage(browser)
        cls.page.url = cls.live_server_url
        cls.page.open()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        super().tearDownClass()

    def test_login_page_title(self):
        """Test the login page title in browser"""
        expected = "Personal Budget App - Login"
        self.assertEqual(expected, self.page.title)
