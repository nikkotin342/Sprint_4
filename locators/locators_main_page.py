from selenium.webdriver.common.by import By


class LocatorsMainPage:
    SEARCH_QUESTION = [By.XPATH, '//*[contains(@id, "accordion__heading-{}")]'] #Найти вопрос
    SEARCH_QUESTION_2 = [By.XPATH, '//*[contains(@id, "accordion__heading-1")]'] #Найти вопрос №2
    SEARCH_ANSWER = [By.XPATH, '//*[contains(@id, "panel-{}")]'] #Найти ответ на вопрос
    SEARCH_ORDER_BUTTON_TOP = [By.XPATH, '//*[contains(@class, "Button_Button") and text()="Заказать"]']  #Кнопка "Заказать" в правом верхнем углу
    SEARCH_SAMOKAT_LOGO = [By.XPATH, '//*[contains(@class, "LogoScooter")]'] #Логотип "Самокат"
    SEARCH_YANDEX_LOGO = [By.XPATH, '//*[contains(@class, "LogoYandex")]'] #Логотип "Яндекс"
    SEARCH_MAIN_PAGE_FIELD = [By.XPATH, '//*[contains(@class, "Home_HomePage")]'] #Стартовая страница сайта
    SEARCH_ORDER_BUTTON_BOTTOM = [By.XPATH, '//*[contains(@class, "Button_Middle") and text() = "Заказать"]']#Кнопка "Заказать" в середине страницы
    SEARCH_DZEN_MAIN_PAGE_FIELD = [By.XPATH, '//*[contains(@aria-label, "Шапка сайта")]'] # Шапка сайта "Дзен"
