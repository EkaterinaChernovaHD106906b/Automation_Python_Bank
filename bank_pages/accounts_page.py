import random
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountsPage(BasePage):
    ACCOUNTS = (By.CSS_SELECTOR, 'a#accounts-index')

    # Excerpt

    EXCERPT = (By.CSS_SELECTOR, 'a#statements-statement')
    ICON_CALENDAR1 = (By.CSS_SELECTOR, 'div#from-date span.add-on i.icon-calendar')
    LIST_OF_DAYS_FROM = (By.XPATH,
                         '//div[@class=\'datepicker datepicker-dropdown dropdown-menu\'][1]//div[@class=\'datepicker-days\']//tbody//td[@class=\'day\']')
    FROM = (By.CSS_SELECTOR, "input[name='from']")
    ICON_CALENDAR2 = (By.CSS_SELECTOR, 'div#until-date i.icon-calendar')
    LIST_OF_DAYS_UNTIL = (By.XPATH,
                          '//div[@class=\'datepicker datepicker-dropdown dropdown-menu\'][2]//div[@class=\'datepicker-days\']//tbody//td[@class=\'day\']')
    UNTIL = (By.CSS_SELECTOR, 'input[name=\'until\']')
    QUERY_BUTTON = (By.CSS_SELECTOR, 'button#query-button')
    HEADERS = (By.CSS_SELECTOR, 'th.header')

    # Current

    CURRENT = (By.CSS_SELECTOR, 'li#accountIndex a#accounts-index')
    SETTINGS = (By.XPATH,
                '//tbody[@id=\'accounts-list-body\']//tr[1]//div[@class=\'btn-group pull-right\']//button[@class=\'btn btn-mini dropdown-toggle\']')
    ORDER_A_CARD = (
        By.XPATH, '//tbody[@id=\'accounts-list-body\']//tr[1]//ul[@class=\'dropdown-menu pull-right\']//li[1]//a')
    LIST_OF_CARDS = (By.CSS_SELECTOR, 'div#single-filters label')
    BUTTONS = (By.CSS_SELECTOR,
               "div[class='cards-group-selection-content span9'] div[class='bordered-card'] div[class='row-fluid row-fluid-wrappable'] button[class='btn btn-primary span5 btn-huge start-order-btn']")
    HEADER = (By.CSS_SELECTOR, 'h2.application-title')
    APPLICATION_TITLE = (By.CSS_SELECTOR, 'h2.application-title')

    # Order a standard card

    STANDARD_CARD_BUTTON = (By.CSS_SELECTOR, 'button[data-ref=\'871\']')
    MODAL = (By.CSS_SELECTOR, 'div[class=\'card-application-modal modal\'] ')
    CHECKBOX1 = (By.CSS_SELECTOR, 'input[name=\'cardOrder.activateSMSNotification\']')
    CHECKBOX2 = (By.CSS_SELECTOR, 'input[name=\'cardOrder.activateInsurance\']')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button#forward')
    LIST_OF_OFFICES = (By.CSS_SELECTOR, 'select[name=\'cardOrder.branch\'] option')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button#confirm')
    IFRAME = (By.CSS_SELECTOR, 'iframe#confirmation-frame')
    ALERT_SUCCESS = (By.CSS_SELECTOR, 'div[class =\'alert alert-success\']')

    def get_excerpt(self):
        accounts = self.element_is_present(self.ACCOUNTS)
        self.move_to_element(accounts)
        self.element_is_visible(self.EXCERPT).click()
        self.element_is_visible(self.ICON_CALENDAR1).click()
        list_of_dates_from = self.elements_are_visible(self.LIST_OF_DAYS_FROM)
        list_of_dates_from[random.randint(0, 16)].click()
        date_from = self.element_is_visible(self.FROM).get_attribute('value')
        self.scroll_by(500)
        self.element_is_visible(self.ICON_CALENDAR2).click()
        list_of_dates_until = self.elements_are_visible(self.LIST_OF_DAYS_UNTIL)
        amount_of_days = len(list_of_dates_until)
        list_of_dates_until[random.randint(0, amount_of_days)].click()
        date_until = self.element_is_visible(self.UNTIL).get_attribute('value')
        self.element_is_visible(self.QUERY_BUTTON).click()
        self.scroll_by(500)
        headers = self.elements_are_visible(self.HEADERS)
        text_headers = [headers[0].text, headers[1].text, headers[2].text, headers[3].text]
        print(f'Date from: {date_from}, date until: {date_until} ')
        return text_headers

    def order_a_card(self):
        accounts = self.element_is_present(self.ACCOUNTS)
        self.move_to_element(accounts)
        self.element_is_visible(self.CURRENT).click()
        self.element_is_visible(self.SETTINGS).click()
        self.element_is_present(self.ORDER_A_CARD).click()
        self.elements_are_visible(self.LIST_OF_CARDS)
        buttons_order_card = self.elements_are_visible(self.BUTTONS)
        buttons_order_card[random.randint(0, 16)].click()

    def order_a_standard_card(self):
        accounts = self.element_is_present(self.ACCOUNTS)
        self.move_to_element(accounts)
        self.element_is_visible(self.CURRENT).click()
        self.element_is_visible(self.SETTINGS).click()
        self.element_is_present(self.ORDER_A_CARD).click()
        self.element_is_visible(self.STANDARD_CARD_BUTTON).click()
        self.element_is_visible(self.MODAL)
        text = self.element_is_visible(self.HEADER).text
        print(text)
        list_of_offices = self.elements_are_presents(self.LIST_OF_OFFICES)
        list_of_offices[random.randint(0, 16)].click()
        self.element_is_visible(self.CHECKBOX1).click()
        self.element_is_visible(self.CHECKBOX2).click()
        self.element_is_visible(self.ORDER_BUTTON).click()
        iframe = self.element_is_present(self.IFRAME)
        self.driver.switch_to.frame(iframe)
        self.element_is_visible(self.CONFIRM_BUTTON).click()
        self.driver.switch_to.default_content()
        text_success = self.element_is_visible(self.ALERT_SUCCESS).text
        return text_success


