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
    SETTINGS = (By.XPATH, '//tbody[@id=\'accounts-list-body\']//tr[1]//div[@class=\'btn-group pull-right\']//button[@class=\'btn btn-mini dropdown-toggle\']')
    ORDER_A_CARD = (By.XPATH, '//tbody[@id=\'accounts-list-body\']//tr[1]//ul[@class=\'dropdown-menu pull-right\']//li[1]//a')

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
