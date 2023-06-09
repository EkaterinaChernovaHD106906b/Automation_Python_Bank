import time
from pages.login_page import LoginPage


class TestBank:
    class TestLoginPage:

        def test_login_page(self, driver):
            login_page = LoginPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
            login_page.open()
            welcome_massage = login_page.enter_like_random_customer()
            time.sleep(3)
            assert welcome_massage == 'Welcome'

        def test_login_definite_customer(self, driver):
            login_page = LoginPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
            login_page.open()
            name = 'Ron'
            name_of_customer = login_page.enter_like_definite_customer(f'{name}')
            balance_before, balance_after = login_page.go_to_deposit_menu()
            time.sleep(5)
            assert name_of_customer == name
            assert balance_before != balance_after

        def test_transactions_menu(self, driver):
            login_page = LoginPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
            login_page.open()
            name = 'Ron'
            login_page.enter_like_definite_customer(f'{name}')
            balance_before, balance_after = login_page.go_to_menu_transactions()
            time.sleep(5)
            assert balance_before != balance_after





