"""
test_login.py
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import tag
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from tests import fixtures
from tests.integration import pom


@tag("integration")
class TestLiveServerBase(StaticLiveServerTestCase):
    """Base live server class"""

    page: pom.BasePage


@tag("integration")
class TestLoginPage(TestLiveServerBase):
    """Test login functionallity"""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.user = fixtures.create_user("demo", "test1234")

        options = Options()
        # Enable this options if you don't want to open the browser
        # options.headless = True
        # options.add_argument("--headless")
        geckodriver = GeckoDriverManager().install()
        service = Service(executable_path=geckodriver)
        cls.browser = Firefox(service=service, options=options)
        cls.page = pom.LoginPage(cls.browser)
        cls.page.url = f"{cls.live_server_url}/users/login"
        cls.page.open()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.page.close()
        super().tearDownClass()

    def test_login_page_title(self):
        """Test the login page title in browser"""
        expected = "Budget Breeze - Login"
        self.assertEqual(expected, self.page.title)

    def test_login_user(self):
        """Test login user form"""

        username_field = pom.BaseElement(self.browser, "id_username", By.ID)
        username_field.input(self.user.username)

        password_field = pom.BaseElement(self.browser, "id_password", By.ID)
        password_field.input("test1234")

        selector = "/html/body/main/div[2]/div/div/form/input[3]"
        submit_btn = pom.BaseElement(self.browser, selector, By.XPATH)

        submit_btn.click()
