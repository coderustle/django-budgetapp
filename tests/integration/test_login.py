"""
test_login.py
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from tests.integration import pom


class TestLiveServerBase(StaticLiveServerTestCase):
    """Base live server class"""

    page: pom.BasePage


class TestLoginPage(TestLiveServerBase):
    """Test login functionallity"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        options = Options()
        # Enable this options if you don't want to open the browser
        # options.headless = True
        # options.add_argument("--headless")
        geckodriver = GeckoDriverManager().install()
        service = Service(executable_path=geckodriver)
        browser = Firefox(service=service, options=options)
        cls.page = pom.LoginPage(browser)
        cls.page.url = f"{cls.live_server_url}/users/login"
        cls.page.open()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        super().tearDownClass()

    def test_login_page_title(self):
        """Test the login page title in browser"""
        expected = "Budget Breeze - Login"
        self.assertEqual(expected, self.page.title)
