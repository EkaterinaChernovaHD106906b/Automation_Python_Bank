import os
import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from generator.generator import generated_file
from pages.base_page import BasePage


class HomePage(BasePage):
    # Menu
    MENU_ELEMENTS = (By.CSS_SELECTOR, 'ul[class="navigation-menu nav"] > li')
    REVIEW = (By.CSS_SELECTOR, 'a#bank-overview')
    ACCOUNTS = (By.CSS_SELECTOR, 'a#accounts-index')
    MAIL = (By.CSS_SELECTOR, 'span.icon-email')

    # Credit
    CREDIT_HREF = (By.XPATH,
                   '//tr[@class=\'offer-for-product type-application APPROVED\']//td[@class=\'right\']//a[@class=\'btn btn-small btn-primary\'][1]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'div.form-actions a')
    OPEN_ACCOUNT_LIST = (By.CSS_SELECTOR, 'select[name="serviceAccountId"] option')
    DATES_LIST = (By.CSS_SELECTOR, 'select[name="repaymentDay"] option')
    CONTINUE_BUTTON2 = (By.CSS_SELECTOR, 'div.form-actions button[class="btn btn-primary"]')
    CHECKBOX_FIRST = (By.CSS_SELECTOR, 'input[name="condition.personalTerms"]')
    CHECKBOX_SECOND = (By.CSS_SELECTOR, 'input[name="condition.insurancePolicy"]')
    CHECKBOX_THIRD = (By.CSS_SELECTOR, 'input[name="condition.insuranceCondition"]')
    CHECKBOX_THOUGH = (By.CSS_SELECTOR, 'input#common-conditions-checkbox')
    ACCEPT_BUTTON = (By.CSS_SELECTOR, 'div[class="modal hidden in"] a#accept-personal-terms-button')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button#confirm')
    DISAGREE = (By.CSS_SELECTOR, 'a#do-not-accept-personal-terms-button')
    IFRAME = (By.CSS_SELECTOR, 'iframe#confirmation-frame')
    TOOLTIP = (By.CSS_SELECTOR, 'div[class="tooltip fade right in"]')

    # Mail

    UNREAD_MESSAGES = (By.CSS_SELECTOR, 'tr[class=\'message-row unread all message\'] td a')
    NEW_MESSAGE = (By.CSS_SELECTOR, 'a#new-message-btn')
    NEW_APPLICATION = (By.CSS_SELECTOR, 'a#new-application-btn')
    THEME = (By.CSS_SELECTOR, 'select[name=\'message.topicName\'] option')
    TEXT_AREA = (By.CSS_SELECTOR, 'textarea[name=\'message.text\']')
    INPUT_FILE = (By.CSS_SELECTOR, 'input[name=\'attachment\']')
    UPLOADED_FILE = (By.XPATH, '//div[@class=\'attachment attachment-block\'][1]// span[@class=\'filename\'][1]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'a#save-message')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class=\'alert alert-success\']')

    def click_on_random_menu_element(self):
        list_of_elements = self.elements_are_presents(self.MENU_ELEMENTS)
        list_of_elements[random.randint(0, 7)].click()

    def get_credit(self):
        self.element_is_visible(self.REVIEW).click()
        self.scroll_by(2000)
        self.element_is_present(self.CREDIT_HREF).click()
        self.element_is_visible(self.CONTINUE_BUTTON).click()
        elements = self.elements_are_presents(self.OPEN_ACCOUNT_LIST)
        accounts = [elements[1], elements[2]]
        accounts[random.randint(0, 1)].click()
        dates = self.elements_are_presents(self.DATES_LIST)
        dates[random.randint(0, 30)].click()
        self.element_is_visible(self.CONTINUE_BUTTON2).click()
        checkbox1 = self.element_is_visible(self.CHECKBOX_FIRST)
        checkbox2 = self.element_is_visible(self.CHECKBOX_SECOND)
        checkbox3 = self.element_is_visible(self.CHECKBOX_THIRD)
        checkbox4 = self.element_is_visible(self.CHECKBOX_THOUGH)
        checkboxes = [checkbox2, checkbox3, checkbox4]
        checkbox1.click()
        self.element_is_visible(self.DISAGREE).click()
        for checkbox in checkboxes:
            checkbox.click()
        iframe = self.element_is_present(self.IFRAME)
        self.driver.switch_to.frame(iframe)
        self.element_is_visible(self.CONFIRM_BUTTON).click()
        self.driver.switch_to.default_content()
        tooltip_text = self.element_is_visible(self.TOOLTIP).text
        return tooltip_text

    def read_messages(self):
        try:
            self.element_is_visible(self.MAIL).click()
            list_of_messages = self.elements_are_visible(self.UNREAD_MESSAGES)
            for message in list_of_messages:
                message.click()
                self.driver.back()
                number_of_unread_messages = len(list_of_messages)
                print(f'Unread emails: {number_of_unread_messages}')
                return number_of_unread_messages
        except TimeoutException:
            print('No unread emails')

    def write_new_message(self):
        self.element_is_visible(self.MAIL).click()
        self.element_is_visible(self.NEW_MESSAGE).click()
        themes = (self.elements_are_presents(self.THEME))
        themes[random.randint(0, 10)].click()
        self.element_is_visible(self.TEXT_AREA).send_keys('Hello, world')
        file_name, path = generated_file()
        self.element_is_present(self.INPUT_FILE).send_keys(path)
        # os.remove(path)
        uploaded_file = self.element_is_visible(self.UPLOADED_FILE).text
        print(f'File {uploaded_file} has been uploaded')
        self.element_is_visible(self.SAVE_BUTTON).click()
        alert_text = self.element_is_visible(self.ALERT_SUCCESS).text
        return alert_text
