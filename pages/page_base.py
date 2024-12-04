import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from tests import help_for_tests


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Вставить текст в поле')
    def add_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение url тестируемого сайта')
    def get_url(self):
        return self.driver.get(help_for_tests.GET_MAIN_URL)

    @allure.step('Форматирование локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

