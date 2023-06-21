from selenium.webdriver.common.by import By

from generator.generator import generated_user
from pages.base_page import BasePage


class RegisterPage(BasePage):
    # registration

    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="customer.firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="customer.lastName"]')
    ADDRESS = (By.CSS_SELECTOR, 'input[id="customer.address.street"]')
    CITY = (By.CSS_SELECTOR, 'input[id="customer.address.city"]')
    STATE = (By.CSS_SELECTOR, 'input[id="customer.address.state"]')
    ZIPCODE = (By.CSS_SELECTOR, 'input[id="customer.address.zipCode"]')
    PHONE = (By.CSS_SELECTOR, 'input[id="customer.phoneNumber"]')
    SSN = (By.CSS_SELECTOR, 'input[id="customer.ssn"]')
    USER_NAME = (By.CSS_SELECTOR, 'input[id="customer.username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="customer.password"]')
    CONFIRM = (By.CSS_SELECTOR, 'input[id="repeatedPassword"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'td input[type="submit"]')
    WELCOME_MASSAGE = (By.CSS_SELECTOR, 'h1.title')

    # login

    USER_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT = (By.CSS_SELECTOR, 'input[type="submit"]')
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, 'h1.title')

    def register_new_user(self):
        user_info = next(generated_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        address = user_info.address
        city = user_info.city
        state = user_info.state
        zipcode = user_info.zipcode
        phone = user_info.phone
        ssn = user_info.ssn
        user_name = user_info.user_name
        password = user_info.password
        self.element_is_visible(self.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.ADDRESS).send_keys(address)
        self.element_is_visible(self.CITY).send_keys(city)
        self.element_is_visible(self.STATE).send_keys(state)
        self.element_is_visible(self.ZIPCODE).send_keys(zipcode)
        self.element_is_visible(self.PHONE).send_keys(phone)
        self.element_is_visible(self.SSN).send_keys(ssn)
        self.element_is_visible(self.USER_NAME).send_keys(user_name)
        self.element_is_visible(self.PASSWORD).send_keys(password)
        self.element_is_visible(self.CONFIRM).send_keys(password)
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        welcome_massage = self.element_is_visible(self.WELCOME_MASSAGE).text
        return user_name, welcome_massage

    def log_in_user(self):
        self.element_is_visible(self.USER_NAME_INPUT).send_keys('user')
        self.element_is_visible(self.PASSWORD_INPUT).send_keys('pass')
        self.element_is_visible(self.SUBMIT).click()
        text = self.element_is_visible(self.SUCCESS_MASSAGE).text
        return text






