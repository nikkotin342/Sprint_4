from locators.locators_main_page import LocatorsMainPage
from pages.page_base import BasePage


class MainPage(BasePage):

    def questions(self,locator_q,locator_a):
        self.click(locator_q)
        self.find_element_with_wait(locator_a)
        return self.find_element_with_wait(locator_a).text

    def scroll(self,driver):
        return self.driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LocatorsMainPage.SEARCH_QUESTION_1))




