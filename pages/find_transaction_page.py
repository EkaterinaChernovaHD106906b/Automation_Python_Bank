import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from pages.base_page import BasePage


class FindTransactionPage(BasePage):
    # search transaction

    FIND_TRANSACTION_HREF = (By.XPATH, '//a[contains(text(),"Find Transactions")]')
    ACCOUNTS_OVERVIEW_LINK = (By.XPATH, '//div[@id="leftPanel"]// li[2]')
    ACCOUNT_NUMBER = (By.CSS_SELECTOR, 'tr.ng-scope td a')
    TRANSACTION_INFO = (By.XPATH, '//tr[@class="ng-scope"][1]//td //a')
    TRANSACTION_ID_INFO = (By.XPATH, '//tr//td[2]')
    AMOUNT = (By.CSS_SELECTOR, 'span[class="ng-binding ng-scope"]')
    SELECT_ACCOUNT = (By.CSS_SELECTOR, 'select#accountId option')
    TRANSACTION_ID = (By.CSS_SELECTOR, 'input[id="criteria.transactionId"]')
    TRANSACTION_DATE = (By.CSS_SELECTOR, 'input[id="criteria.onDate"]')
    DATE_RANGE1 = (By.CSS_SELECTOR, 'input[id="criteria.fromDate"]')
    DATE_RANGE2 = (By.CSS_SELECTOR, 'input[id="criteria.toDate"]')
    SUM = (By.CSS_SELECTOR, 'input[id="criteria.amount"]')
    BUTTON_FIND_BY_AMOUNT = (By.XPATH, '//form//div[9]//button[@type="submit"]')
    BUTTON_FIND_BY_DATE = (By.XPATH, '//form//div[5]//button')
    BUTTON_FIND_BY_DATE_RANGE = (By.XPATH, '//form//div[7]//button')
    BUTTON_FIND_BY_ID = (By.XPATH, '//form//div[3]//button')
    TRANSACTION_RESULTS = (By.CSS_SELECTOR, 'h1.title')

    # transfer funds

    TRANSFER_FUNDS_HREF = (By.XPATH, '//a[contains(text(),"Transfer")]')
    ACCOUNT_SELECT = (By.CSS_SELECTOR, 'select#fromAccountId')
    AMOUNT_TRANSFER = (By.CSS_SELECTOR, 'input#amount')
    TRANSFER_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    def find_transaction_by_amount(self):
        self.element_is_visible(self.TRANSFER_FUNDS_HREF).click()
        random_amount = random.randint(1000, 100000)
        self.element_is_visible(self.AMOUNT_TRANSFER).send_keys(random_amount)
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select#fromAccountId')).select_by_index(0)
        self.element_is_visible(self.TRANSFER_BUTTON).click()
        self.element_is_visible(self.FIND_TRANSACTION_HREF).click()
        element = self.element_is_visible(self.AMOUNT)
        self.move_to_element(element)
        element.send_keys(random_amount)
        self.scroll_by(200)
        self.element_is_visible(self.BUTTON_FIND_BY_AMOUNT).click()
        time.sleep(3)
        result = self.element_is_visible(self.TRANSACTION_RESULTS).text
        return result

    def find_transaction_by_date(self):
        date_info = next(generated_date())
        date = [date_info.day, date_info.month, date_info.year]
        self.element_is_visible(self.FIND_TRANSACTION_HREF).click()
        self.element_is_visible(self.TRANSACTION_DATE).send_keys(date[0] + '-' + date[1] + '-' + date[2])
        self.element_is_visible(self.BUTTON_FIND_BY_DATE).click()
        time.sleep(3)
        result = self.element_is_visible(self.TRANSACTION_RESULTS).text
        return result

    def find_transaction_by_date_range(self):
        date_info = next(generated_date())
        day = date_info.day
        month = date_info.month
        year = date_info.year
        date1 = [day, month, year]
        self.element_is_visible(self.FIND_TRANSACTION_HREF).click()
        self.element_is_visible(self.DATE_RANGE1).send_keys(date1[0] + '-' + date1[1] + '-' + date1[2])
        date_info2 = next(generated_date())
        day2 = date_info2.day
        month2 = date_info2.month
        year2 = date_info2.year
        date2 = [day2, month2, year2]
        self.element_is_visible(self.DATE_RANGE2).send_keys(date2[0] + '-' + date2[1] + '-' + date2[2])
        self.element_is_visible(self.BUTTON_FIND_BY_DATE_RANGE).click()
        time.sleep(3)
        result = self.element_is_visible(self.TRANSACTION_RESULTS).text
        return result

    def find_transaction_by_id(self):
        self.element_is_visible(self.ACCOUNTS_OVERVIEW_LINK).click()
        self.element_is_visible(self.ACCOUNT_NUMBER).click()
        self.element_is_visible(self.TRANSACTION_INFO).click()
        id_info = self.element_is_visible(self.TRANSACTION_ID_INFO).text
        self.element_is_visible(self.FIND_TRANSACTION_HREF).click()
        self.element_is_visible(self.TRANSACTION_ID).send_keys(id_info)
        self.element_is_visible(self.BUTTON_FIND_BY_ID).click()
        time.sleep(3)
        amount = self.element_is_visible(self.AMOUNT).text
        return amount












