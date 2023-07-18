import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # Menu
    MENU_ELEMENTS = (By.CSS_SELECTOR, 'ul[class="navigation-menu nav"] > li')
    REVIEW = (By.CSS_SELECTOR, 'a#bank-overview')
    ACCOUNTS = (By.CSS_SELECTOR, 'a#accounts-index')

    # Credit
    CREDIT_HREF = (By.XPATH, '//tr[@class=\'offer-for-product type-application APPROVED\']//td[@class=\'right\']//a[@class=\'btn btn-small btn-primary\'][1]')
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











