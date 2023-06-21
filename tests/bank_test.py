import time

from pages.account_services_page import AccountServicesPage
from pages.customer_page import LoginPage
from pages.manager_page import ManagerPage
from pages.register_page import RegisterPage


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

        def test_add_new_customer(self, driver):
            manager_page = ManagerPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
            manager_page.open()
            alert_text = manager_page.add_new_customer()
            time.sleep(5)
            assert alert_text == 'Customer added successfully with customer id :6'

        def test_delete_added_customer(self, driver):
            manager_page = ManagerPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
            manager_page.open()
            quantity_of_customers_before, quantity_of_customers_after = manager_page.delete_customer()
            time.sleep(5)
            assert quantity_of_customers_before != quantity_of_customers_after

        def test_open_account(self, driver):
            manager_page = ManagerPage(driver, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount')
            manager_page.open()
            alert_info = manager_page.open_account()
            time.sleep(5)
            assert alert_info == 'Account created successfully with account Number :1016'

        def test_register_new_user(self, driver):
            register_page = RegisterPage(driver, 'https://parabank.parasoft.com/parabank/register.htm')
            register_page.open()
            user_name, welcome_massage = register_page.register_new_user()
            time.sleep(5)
            assert welcome_massage == f'Welcome {user_name}'

        def test_login(self, driver):
            register_page = RegisterPage(driver, 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')
            register_page.open()
            text = register_page.log_in_user()
            assert text == 'Accounts Overview'

        def test_open_new_account(self, driver):
            register_page = RegisterPage(driver, 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')
            register_page.open()
            register_page.log_in_user()
            services_page = AccountServicesPage(driver, 'https://parabank.parasoft.com/parabank/openaccount.htm')
            success_massage = services_page.open_new_account()
            time.sleep(3)
            assert success_massage == 'Congratulations, your account is now open.'



