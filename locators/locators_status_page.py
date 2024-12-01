from selenium.webdriver.common.by import By


class LocatorsStatusPage:
    SEARCH_STATUS_ORDER_FIELD = [By.XPATH, '//*[contains(@class, "Track_Title") and text()="Имя"]'] # Поле Имя в инфо про заказ
    SEARCH_SAMOKAT_LOGO = [By.XPATH, '//*[contains(@class, "LogoScooter")]']  # Логотип "Самокат"