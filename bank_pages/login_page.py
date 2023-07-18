import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    INPUT_USER_NAME = (By.CSS_SELECTOR, 'div input[name="username"]')
    INPUT_PASS = (By.CSS_SELECTOR, 'div input[name="password"]')
    SHOW_PASSWORD = (By.CSS_SELECTOR, ' svg[class="eye-on"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button#login-button')
    ACCESS_RECOVERY = (By.CSS_SELECTOR, ' div#additional-actions a.chevron')
    MODAL_TEXT = (By.XPATH, '//h3[contains(text(),"Забыли логин")]')
    INPUT_CODE = (By.CSS_SELECTOR, 'input#otp-code')
    BUTTON_CODE = (By.CSS_SELECTOR, 'button#login-otp-button')
    MENU = (By.CSS_SELECTOR, 'a#bank-overview')

    def login_user(self, user, password):
        user_name = self.element_is_visible(self.INPUT_USER_NAME)
        user_name.clear()
        user_name.send_keys(user)
        input_pass = self.element_is_visible(self.INPUT_PASS)
        input_pass.clear()
        input_pass.send_keys(password)
        self.element_is_visible(self.SHOW_PASSWORD).click()
        self.element_is_visible(self.LOGIN_BUTTON).click()
        input_code = self.element_is_visible(self.INPUT_CODE)
        input_code.clear()
        input_code.send_keys('0000')
        self.element_is_visible(self.BUTTON_CODE).click()
        menu_text = self.element_is_visible(self.MENU).text
        return menu_text

    def check_recovery_access_alert(self):
        self.element_is_visible(self.ACCESS_RECOVERY).click()
        text = self.element_is_visible(self.MODAL_TEXT).text
        return text





