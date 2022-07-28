from .locators import BasePageLocators as BP_locators
from selenium.common.exceptions import (
    NoSuchElementException,
)


class BasePage():
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except (NoSuchElementException):
            return False
        return True

    def to_search_page(self):
        search_page_link = self.driver.find_element(*BP_locators.SEARCH_PAGE_LINK)
        search_page_link.click()
