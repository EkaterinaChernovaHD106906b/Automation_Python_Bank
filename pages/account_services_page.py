import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class AccountServicesPage(BasePage):
    OPEN_NEW_ACCOUNT_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[1]')
    ACCOUNTS_OVERVIEW_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[2]')
    TRANSFER_FUNDS_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[3]')
    BILL_PAY_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[4]')
    FIND_TRANSACTIONS_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[5]')
    UPDATE_CONTACT_INFO_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[6]')
    REQUEST_LOAN_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[7]')

    # Open new account

    BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    SUCCESS_MASSAGE = (By.XPATH, '//div[@ng-if="showResult"]//p[1]')

    def open_new_account(self):
        self.element_is_visible(self.OPEN_NEW_ACCOUNT_LINK).click()
        values_type = ('0', '1')
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#type')).select_by_value(values_type[random.randint(0, 1)])
        time.sleep(3)
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#fromAccountId')).select_by_index(0)
        self.element_is_visible(self.BUTTON).click()
        success_massage = self.element_is_visible(self.SUCCESS_MASSAGE).text
        return success_massage


