"""
Page object model.
"""
from typing import Optional

from selenium.webdriver import Firefox


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
