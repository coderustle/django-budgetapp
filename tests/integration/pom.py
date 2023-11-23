"""
Page object model.
"""
from collections import namedtuple
from typing import Optional

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base page to be inherited by other pages

    Public attributes:
    """

    url: Optional[str] = None

    def __init__(self, driver: Firefox):
        self.driver = driver

    def open(self):
        """Open the browser with the given url"""
        self.driver.get(url=self.url)

    def close(self):
        """Close the browser"""
        self.driver.quit()

    def url_contains(self, url: str):
        """Return the current url after redirection"""
        condition = EC.url_contains(url=url)
        result = WebDriverWait(self.driver, 10).until(condition)
        return result

    def previous(self):
        """Request browser to go to the previous page"""
        self.driver.execute_script("window.history.go(-1)")

    def switch_to_main_window(self):
        """Check if how many tabs are and return to the first one"""
        windows = self.driver.window_handles
        if len(windows) > 1:
            main_window = self.driver.window_handles[0]
            self.driver.switch_to.window(main_window)


class BaseElement:
    """Describe a base element
    Public attributes:
    - driver: The browser driver used to manipulate the element
    - locator: A named tuple with selector and selector type
    - selector: The value for element selector
    - sel_type: The selector type provided in By enum
    Public properties:
    - element: A property that return the element
    """

    Locator: tuple = namedtuple("Locator", ["by", "value"])

    def __init__(self, driver: Firefox, selector: str, sel_type: By) -> None:
        self.driver = driver
        self.Locator.by = sel_type
        self.Locator.value = selector
        self.element = self.find()

    def find(self) -> WebElement:
        """Return an element"""
        locator = (self.Locator.by, self.Locator.value)
        condition = EC.visibility_of_element_located(locator=locator)
        element = WebDriverWait(self.driver, 10).until(condition)
        return element

    def click(self) -> None:
        """Click on the element"""
        self.element.click()

    def text(self) -> str:
        """Return the text of an element"""
        return self.element.text

    def input(self, value) -> None:
        """Add input text"""
        self.element.send_keys(value)


class LoginPage(BasePage):
    """This class represents the login page"""

    @property
    def title(self):
        """Return the page title"""
        return self.driver.title
