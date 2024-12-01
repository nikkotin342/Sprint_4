from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import help_for_tests


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def add_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_url(self):
        return self.driver.get(help_for_tests.GET_MAIN_URL)

