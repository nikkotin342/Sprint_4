import allure

from pages.page_base import BasePage


class OrderPage(BasePage):

    @allure.step('Оформление заказа')
    def order(self, locator_order, locator_name, text1, locator_surname,text2, locator_city,text3, locator_metro1, locator_metro2, locator_phone,text4, locator_con,
              locator_data, locator_day, locator_rent, locator_count, locator_color,
              locator_order_button, locator_yes, locator_status):
        self.click(locator_order)
        self.add_text(locator_name,text1)
        self.add_text(locator_surname, text2)
        self.add_text(locator_city, text3)
        self.click(locator_metro1)
        self.click(locator_metro2)
        self.add_text(locator_phone, text4)
        self.click(locator_con)
        self.click(locator_data)
        self.click(locator_day)
        self.click(locator_rent)
        self.click(locator_count)
        self.click(locator_color)
        self.click(locator_order_button)
        self.find_element_with_wait(locator_yes)
        self.click(locator_yes)
        self.click(locator_status)
        

    @allure.step('Клик на лого самоката')
    def go_to_samokat(self, locator_samokat):
        self.click(locator_samokat)


    @allure.step('Клик на лого Яндекса')
    def go_to_dzen(self, locator_ya, driver):    
        self.click(locator_ya)
        driver.switch_to.window(driver.window_handles[1])
        
        
