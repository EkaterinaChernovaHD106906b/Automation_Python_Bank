import time

from bank_pages.accounts_page import AccountsPage
from bank_pages.home_page import HomePage
from bank_pages.login_page import LoginPage


class TestBSPBBank:
    class TestDemo:
        def test_login_page(self, driver):
            login_page = LoginPage(driver, 'https://idemo.bspb.ru/')
            login_page.open()
            result = login_page.login_user('demo', 'demo')
            assert result == 'ОБЗОР'

        def test_access_recovery_message(self, driver):
            login_page = LoginPage(driver, 'https://idemo.bspb.ru/')
            login_page.open()
            message_text = login_page.check_recovery_access_alert()
            assert message_text == 'Забыли логин или пароль?'

        def test_home_page(self, driver):
            home_page = HomePage(driver, 'https://idemo.bspb.ru/welcome')
            login_page = LoginPage(driver, 'https://idemo.bspb.ru/')
            login_page.open()
            login_page.login_user('demo', 'demo')
            home_page.click_on_random_menu_element()

        def test_get_credit(self, driver):
            home_page = HomePage(driver, 'https://idemo.bspb.ru/welcome')
            login_page = LoginPage(driver, 'https://idemo.bspb.ru/')
            login_page.open()
            login_page.login_user('demo', 'demo')
            tooltip_text = home_page.get_credit()
            assert tooltip_text == 'Обязательное поле'

        def test_get_excerpt(self, driver):
            login_page = LoginPage(driver, 'https://idemo.bspb.ru/')
            login_page.open()
            accounts_page = AccountsPage(driver, 'https://idemo.bspb.ru/statement')
            login_page.login_user('demo', 'demo')
            result_table = accounts_page.get_excerpt()
            assert result_table == ['Дата', 'Плательщик / Получатель', 'Операция', 'Сумма (RUB)']






