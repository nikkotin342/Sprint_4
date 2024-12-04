from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    SEARCH_NAME_FIELD = [By.XPATH, '//*[contains(@placeholder, "* Имя")]'] # Поле "Имя"
    SEARCH_SURNAME_FIELD = [By.XPATH, '//*[contains(@placeholder, "* Фамилия")]'] # Поле "Фамилия"
    SEARCH_CITY_FIELD = [By.XPATH, '//*[contains(@placeholder, "* Адрес: куда привезти заказ")]'] # Поле "Город"
    SEARCH_METRO_FIELD = [By.XPATH, '//*[contains(@class, "select-search__value")]'] # Поле "Метро"
    SEARCH_METRO_BUTTON = [By.XPATH, '//*[contains(@class, "select-search__select")]'] # Выбрать Метро
    SEARCH_PHONE_NUMBER_FIELD = [By.XPATH, '//*[contains(@placeholder, "* Телефон: на него позвонит курьер")]'] # Поле "Номер телефона"
    SEARCH_CONTINUE_BUTTON = [By.XPATH, '//*[contains(@class,"Button_Middle")]'] # Кнопка "Далее"
    SEARCH_DATA_FIELD = [By.XPATH, '//*[contains(@placeholder, "* Когда привезти самокат")]'] # Поле "Когда привезти"
    SEARCH_DAY_BUTTON = [By.XPATH, '//*[contains(@aria-label, "29-е декабря")]'] # Кнопка "29 декабря"
    SEARCH_RENT_FIELD = [By.XPATH, '//*[contains(@class, "Dropdown") and text()="* Срок аренды"]'] # Поле "Срок аренды"
    SEARCH_COUNT1_RENT_BUTTON = [By.XPATH, '//*[contains(@class, "Dropdown") and text()="сутки"]'] # Кнопка "Сутки"
    SEARCH_COUNT2_RENT_BUTTON = [By.XPATH, '//*[contains(@class, "Dropdown") and text()="двое суток"]']  # Кнопка "Двое суток"
    SEARCH_COLOUR1_FIELD = [By.XPATH, '//*[contains(@class, "Checkbox") and text()="чёрный жемчуг"]'] # Поле "черный жемчуг"
    SEARCH_COLOUR2_FIELD = [By.XPATH, '//*[contains(@class, "Checkbox") and text()="серая безысходность"]']  # Поле "серая безысходность"
    SEARCH_ORDER_BUTTON = [By.XPATH, '//*[contains(@class,"Button_Middle") and text()="Заказать"]'] # Кнопка "Заказать"
    SEARCH_YESORNO_FIELD = [By.XPATH, '//*[contains(@class,"Order_ModalHeader")]']  # Поле "Вы хотите сделать заказ?"
    SEARCH_YES_BUTTON = [By.XPATH, '//*[contains(@class, "Button_Middle")and text()="Да"]'] # Кнопка "Да"
    SEARCH_ORDER_INFO_FIELD = [By.XPATH, '//*[contains(@class, "Order_ModalHeader")]'] # Поле "Посмотреть статус заказа"
    SEARCH_STATUS_BUTTON = [By.XPATH, '//*[contains(@class, "Button_Middle")and text()="Посмотреть статус"]'] # Кнопка "Посмотреть статус"
