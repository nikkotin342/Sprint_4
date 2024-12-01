import pytest


from locators.locators_main_page import LocatorsMainPage
from pages.page_main import MainPage


class TestQuest:


    def test_quest_1(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_1, LocatorsMainPage.SEARCH_ANSWER_1) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'


    def test_quest_2(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_2, LocatorsMainPage.SEARCH_ANSWER_2) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'


    def test_quest_3(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_3, LocatorsMainPage.SEARCH_ANSWER_3) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    def test_quest_4(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_4, LocatorsMainPage.SEARCH_ANSWER_4) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


    def test_quest_5(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_5, LocatorsMainPage.SEARCH_ANSWER_5) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'


    def test_quest_6(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_6, LocatorsMainPage.SEARCH_ANSWER_6) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'


    def test_quest_7(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_7, LocatorsMainPage.SEARCH_ANSWER_7) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'


    def test_quest_8(self,driver):
        main_page = MainPage(driver)
        main_page.get_url()
        main_page.scroll(driver)
        assert main_page.questions(LocatorsMainPage.SEARCH_QUESTION_8, LocatorsMainPage.SEARCH_ANSWER_8) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        

