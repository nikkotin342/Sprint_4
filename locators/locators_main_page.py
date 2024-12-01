from selenium.webdriver.common.by import By


class LocatorsMainPage:
    SEARCH_QUESTION_1 = [By.XPATH, '//*[contains(@id, "accordion__heading-0")]'] #Найти вопрос №1
    SEARCH_QUESTION_2 = [By.XPATH, '//*[contains(@id, "accordion__heading-1")]'] #Найти вопрос №2
    SEARCH_QUESTION_3 = [By.XPATH, '//*[contains(@id, "accordion__heading-2")]'] #Найти вопрос №3
    SEARCH_QUESTION_4 = [By.XPATH, '//*[contains(@id, "accordion__heading-3")]'] #Найти вопрос №4
    SEARCH_QUESTION_5 = [By.XPATH, '//*[contains(@id, "accordion__heading-4")]'] #Найти вопрос №5
    SEARCH_QUESTION_6 = [By.XPATH, '//*[contains(@id, "accordion__heading-5")]'] #Найти вопрос №6
    SEARCH_QUESTION_7 = [By.XPATH, '//*[contains(@id, "accordion__heading-6")]'] #Найти вопрос №7
    SEARCH_QUESTION_8 = [By.XPATH, '//*[contains(@id, "accordion__heading-7")]'] #Найти вопрос №8
    SEARCH_ANSWER_1 = [By.XPATH, '//*[contains(@id, "panel-0")]'] #Найти ответ на вопрос №1
    SEARCH_ANSWER_2 = [By.XPATH, '//*[contains(@id, "panel-1")]'] #Найти ответ на вопрос №2
    SEARCH_ANSWER_3 = [By.XPATH, '//*[contains(@id, "panel-2")]'] #Найти ответ на вопрос №3
    SEARCH_ANSWER_4 = [By.XPATH, '//*[contains(@id, "panel-3")]'] #Найти ответ на вопрос №4
    SEARCH_ANSWER_5 = [By.XPATH, '//*[contains(@id, "panel-4")]'] #Найти ответ на вопрос №5
    SEARCH_ANSWER_6 = [By.XPATH, '//*[contains(@id, "panel-5")]'] #Найти ответ на вопрос №6
    SEARCH_ANSWER_7 = [By.XPATH, '//*[contains(@id, "panel-6")]'] #Найти ответ на вопрос №7
    SEARCH_ANSWER_8 = [By.XPATH, '//*[contains(@id, "panel-7")]'] #Найти ответ на вопрос №8
    SEARCH_ORDER_BUTTON_TOP = [By.XPATH, '//*[contains(@class, "Button_Button") and text()="Заказать"]']  #Кнопка "Заказать" в правом верхнем углу
    SEARCH_SAMOKAT_LOGO = [By.XPATH, '//*[contains(@class, "LogoScooter")]'] #Логотип "Самокат"
    SEARCH_YANDEX_LOGO = [By.XPATH, '//*[contains(@class, "LogoYandex")]'] #Логотип "Яндекс"
    SEARCH_MAIN_PAGE_FIELD = [By.XPATH, '//*[contains(@class, "Home_HomePage")]'] #Стартовая страница сайта
    SEARCH_ORDER_BUTTON_BOTTOM = [By.XPATH, '//*[contains(@class, "Button_Middle") and text() = "Заказать"]']#Кнопка "Заказать" в середине страницы
    SEARCH_DZEN_MAIN_PAGE_FIELD = [By.XPATH, '//*[contains(@aria-label, "Шапка сайта")]'] # Шапка сайта "Дзен"
