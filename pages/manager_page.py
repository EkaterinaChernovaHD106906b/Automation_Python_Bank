import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_customer
from pages.base_page import BasePage


class ManagerPage(BasePage):
    # Login

    BANK_MANAGER_LOGIN = (By.XPATH, '//div[@class="borderM box padT20"]//div[2]//button')

    # Menu

    ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
    OPEN_ACCOUNT = (By.XPATH, '//div[@class="center"]//button[2]')
    CUSTOMERS = (By.XPATH, '//div[@class="center"]//button[3]')

    # Add customer

    INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    POST_CODE = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    # Delete customer

    LIST_OF_CUSTOMERS = (By.CSS_SELECTOR, 'tr[class="ng-scope"]')
    DELETE_CUSTOMER = (By.XPATH, '//tr[6]//button[@ng-click="deleteCust(cust)"]')

    def add_new_customer(self):
        self.element_is_visible(self.BANK_MANAGER_LOGIN).click()
        self.element_is_visible(self.ADD_CUSTOMER).click()
        customer_info = next(generated_customer())
        first_name = customer_info.first_name
        last_name = customer_info.last_name
        post_code = customer_info.post_code
        self.element_is_visible(self.INPUT_FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.INPUT_LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.POST_CODE).send_keys(post_code)
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def delete_customer(self):
        self.add_new_customer()
        self.element_is_visible(self.CUSTOMERS).click()
        list_of_customers = self.elements_are_visible(self.LIST_OF_CUSTOMERS)
        quantity_of_customers_before = len(list_of_customers)
        added_customer = list_of_customers[5]
        info_added_customer = added_customer.text
        info = info_added_customer.split()
        name_of_added_customer = info[0]
        surname_of_added_customer = info[1]
        self.element_is_visible(self.DELETE_CUSTOMER).click()
        new_list = self.elements_are_visible(self.LIST_OF_CUSTOMERS)
        quantity_of_customers_after = len(new_list)
        print(f'{name_of_added_customer} {surname_of_added_customer} was deleted ')
        return quantity_of_customers_before, quantity_of_customers_after

    def open_account(self):
        self.element_is_visible(self.OPEN_ACCOUNT).click()
        list_of_values = ['1', '2', '3', '4', '5']
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#userSelect')).select_by_value(list_of_values[random.randint(0, 4)])
        list_of_currency = ['Dollar', 'Pound', 'Rupee']
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#currency')).select_by_value(list_of_currency[random.randint(0, 2)])
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert_info = alert.text
        alert.accept()
        return alert_info

