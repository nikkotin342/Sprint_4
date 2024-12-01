import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page import LocatorsMainPage
from locators.locators_order_page import LocatorsOrderPage
from locators.locators_status_page import LocatorsStatusPage
from pages.page_order import OrderPage
from tests import help_for_tests


class TestOrder():
    @pytest.mark.parametrize("name,surname,city", [['Саша', 'Ваш', 'Москва']])
    def test_order_button_top(self, driver, phone, name, surname, city):
        order_page=OrderPage(driver)
        order_page.get_url()
        order_page.order(LocatorsMainPage.SEARCH_ORDER_BUTTON_TOP,LocatorsOrderPage.SEARCH_NAME_FIELD,name,LocatorsOrderPage.SEARCH_SURNAME_FIELD,surname,LocatorsOrderPage.SEARCH_CITY_FIELD,city,LocatorsOrderPage.SEARCH_METRO_FIELD,LocatorsOrderPage.SEARCH_METRO_BUTTON,LocatorsOrderPage.SEARCH_PHONE_NUMBER_FIELD,phone,LocatorsOrderPage.SEARCH_CONTINUE_BUTTON,LocatorsOrderPage.SEARCH_DATA_FIELD,LocatorsOrderPage.SEARCH_DAY_BUTTON,LocatorsOrderPage.SEARCH_RENT_FIELD,LocatorsOrderPage.SEARCH_COUNT1_RENT_BUTTON,LocatorsOrderPage.SEARCH_COLOUR1_FIELD,LocatorsOrderPage.SEARCH_ORDER_BUTTON,LocatorsOrderPage.SEARCH_YES_BUTTON,LocatorsOrderPage.SEARCH_STATUS_BUTTON)
        assert order_page.find_element_with_wait(LocatorsStatusPage.SEARCH_STATUS_ORDER_FIELD)
        order_page.go_to_samokat(LocatorsStatusPage.SEARCH_SAMOKAT_LOGO)
        assert order_page.find_element_with_wait(LocatorsMainPage.SEARCH_MAIN_PAGE_FIELD)
        order_page.go_to_dzen(LocatorsMainPage.SEARCH_YANDEX_LOGO,driver)
        assert order_page.find_element_with_wait(LocatorsMainPage.SEARCH_DZEN_MAIN_PAGE_FIELD)

    @pytest.mark.parametrize("name,surname,city", [['Маша', 'Наша', 'Москва']])
    def test_order_button_bottom(self, driver, phone, name, surname, city):
        order_page = OrderPage(driver)
        order_page.get_url()
        order_page.order(LocatorsMainPage.SEARCH_ORDER_BUTTON_TOP, LocatorsOrderPage.SEARCH_NAME_FIELD, name,
                         LocatorsOrderPage.SEARCH_SURNAME_FIELD, surname, LocatorsOrderPage.SEARCH_CITY_FIELD, city,
                         LocatorsOrderPage.SEARCH_METRO_FIELD, LocatorsOrderPage.SEARCH_METRO_BUTTON,
                         LocatorsOrderPage.SEARCH_PHONE_NUMBER_FIELD, phone, LocatorsOrderPage.SEARCH_CONTINUE_BUTTON,
                         LocatorsOrderPage.SEARCH_DATA_FIELD, LocatorsOrderPage.SEARCH_DAY_BUTTON,
                         LocatorsOrderPage.SEARCH_RENT_FIELD, LocatorsOrderPage.SEARCH_COUNT2_RENT_BUTTON,
                         LocatorsOrderPage.SEARCH_COLOUR2_FIELD, LocatorsOrderPage.SEARCH_ORDER_BUTTON,
                         LocatorsOrderPage.SEARCH_YES_BUTTON, LocatorsOrderPage.SEARCH_STATUS_BUTTON)
        assert order_page.find_element_with_wait(LocatorsStatusPage.SEARCH_STATUS_ORDER_FIELD)
        order_page.go_to_samokat(LocatorsStatusPage.SEARCH_SAMOKAT_LOGO)
        assert order_page.find_element_with_wait(LocatorsMainPage.SEARCH_MAIN_PAGE_FIELD)
        order_page.go_to_dzen(LocatorsMainPage.SEARCH_YANDEX_LOGO, driver)
        assert order_page.find_element_with_wait(LocatorsMainPage.SEARCH_DZEN_MAIN_PAGE_FIELD)

