import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Login

    CUSTOMER_LOGIN = (By.XPATH, '//div[@class="borderM box padT20"]//div[1]//button')
    BANK_MANAGER_LOGIN = (By.XPATH, '//div[@class="borderM box padT20"]//div[2]//button')
    LOGOUT = (By.CSS_SELECTOR, 'button[class="btn logout"]')

    # Customers

    SELECT = (By.CSS_SELECTOR, 'select#userSelect')
    SELECT_LIST = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    WELCOME_MASSAGE = (By.XPATH, '//div[@class="borderM box padT20 ng-scope"]//div//strong')
    GRANGER = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat][value="1"]')
    POTTER = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat][value="2"]')
    WEASLY = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat][value="3"]')
    DUMBLEDORE = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat][value="4"]')
    LONGBOTTOM = (By.CSS_SELECTOR, 'select[id="userSelect"] option[ng-repeat][value="5"]')
    NAME = (By.CSS_SELECTOR, 'div[class="borderM box padT20 ng-scope"] span[class="fontBig ng-binding"]')

    # Menu

    LIST_ACCOUNT_NUMBERS = (By.CSS_SELECTOR, 'select#accountSelect option')
    TRANSACTIONS = (By.XPATH, '//div[@class="center"]//button[1]')
    DEPOSITS = (By.XPATH, '//div[@class="center"]//button[2]')
    WITHDRAWL = (By.XPATH, '//div[@class="center"]//button[3]')
    BUTTON_BACK = (By.CSS_SELECTOR, 'button[ng-click="back()"]')

    # Deposits

    DEPOSIT_INPUT = (By.CSS_SELECTOR, 'input[type="number"]')
    DEPOSIT_MASSAGE = (By.CSS_SELECTOR, 'span[class="error ng-binding"]')
    BALANCE = (By.XPATH, '//div[@class="borderM box padT20 ng-scope"]//div[@class="center"][1]//strong[2]')

    # Transactions

    LIST_OF_TRANSACTIONS = (By.CSS_SELECTOR, 'tbody tr')

    def enter_like_random_customer(self):
        self.element_is_visible(self.CUSTOMER_LOGIN).click()
        time.sleep(5)
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value(
            f'{random.randint(0, 4)}')
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        welcome_massage = self.element_is_visible(self.WELCOME_MASSAGE).text
        list_ms = welcome_massage.split()
        el = list_ms[0]
        self.element_is_visible(self.LOGOUT).click()
        return el

    def enter_like_definite_customer(self, name):
        self.element_is_visible(self.CUSTOMER_LOGIN).click()
        time.sleep(5)
        names_of_customers = ['Hermoine', 'Harry', 'Ron', 'Albus', 'Neville']
        if name == names_of_customers[0]:
            Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value('1')
        if name == names_of_customers[1]:
            Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value('2')
        if name == names_of_customers[2]:
            Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value('3')
        if name == names_of_customers[3]:
            Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value('4')
        if name == names_of_customers[4]:
            Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="userSelect"]')).select_by_value('5')
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        welcome_massage = self.element_is_visible(self.NAME).text
        list_ms = welcome_massage.split()
        name_customer = list_ms[0]
        # self.element_is_visible(self.LOGOUT).click()
        return name_customer

    def go_to_deposit_menu(self):
        list_of_accounts_numbers = ['number:1007', 'number:1008', 'number:1009']
        Select(self.driver.find_element(By.CSS_SELECTOR, 'select[id="accountSelect"]')).select_by_value(
            list_of_accounts_numbers[random.randint(0, 2)])
        self.element_is_visible(self.DEPOSITS).click()
        balance_before = self.element_is_visible(self.BALANCE).text
        self.element_is_visible(self.DEPOSIT_INPUT).send_keys(random.randint(100, 60000))
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        deposit_massage = self.element_is_visible(self.DEPOSIT_MASSAGE).text
        print(deposit_massage)
        balance_after = self.element_is_visible(self.BALANCE).text
        return balance_before, balance_after

    def go_to_menu_transactions(self):
        self.element_is_visible(self.DEPOSITS).click()
        balance_before = self.element_is_visible(self.BALANCE).text
        count = 3
        while count != 0:
            self.element_is_visible(self.DEPOSIT_INPUT).send_keys(random.randint(100, 60000))
            self.element_is_visible(self.SUBMIT_BUTTON).click()
            count -= 1
        self.element_is_visible(self.TRANSACTIONS).click()
        self.element_is_visible(self.BUTTON_BACK).click()
        self.element_is_visible(self.WITHDRAWL).click()
        self.element_is_visible(self.DEPOSIT_INPUT).send_keys(random.randint(1000, 10000))
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        balance_after = self.element_is_visible(self.BALANCE).text
        self.element_is_visible(self.TRANSACTIONS).click()
        time.sleep(3)
        self.driver.refresh()

        list_of_transactions = self.elements_are_presents(self.LIST_OF_TRANSACTIONS)
        quantity_of_transactions = len(list_of_transactions)
        print(f'Quantity of transactions: {quantity_of_transactions}' + ' ' + f'Balance before: {balance_before}, balance after: {balance_after}')
        # first_transaction = list_of_transactions[0]
        # second_transaction = list_of_transactions[1]
        # third_transaction = list_of_transactions[2]
        # forth_transaction = list_of_transactions[3]
        info_first_transaction = list_of_transactions[0].text
        info_first = info_first_transaction.split()
        amount_first = info_first[5]
        info_second_transaction = list_of_transactions[1].text
        info_second = info_second_transaction.split()
        amount_second = info_second[5]
        info_third_transaction = list_of_transactions[2].text
        info_third = info_third_transaction.split()
        amount_third = info_third[5]
        info_forth_transaction = list_of_transactions[3].text
        info_forth = info_forth_transaction.split()
        amount_forth = info_forth[5]
        print(' ' + f'Amount of first transaction: {amount_first},\n amount of second transaction: {amount_second}, \n amount of third transaction: {amount_third}, \n amount of fourth transaction: {amount_forth}')
        return balance_before, balance_after
