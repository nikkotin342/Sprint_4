import allure

from locators.locators_main_page import LocatorsMainPage
from pages.page_base import BasePage


class MainPage(BasePage):
    @allure.step('Скролл до вопросов')
    def scroll(self,driver):
        return self.driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LocatorsMainPage.SEARCH_QUESTION_2))

    @allure.step('Выбор вопроса из списка и проверка полученного ответа')
    def questions(self,locator_q,locator_a, num):
        locator_q_forr = self.format_locators(locator_q,num)
        locator_a_forr = self.format_locators(locator_a,num)
        self.click(locator_q_forr)
        return self.find_element_with_wait(locator_a_forr).text






