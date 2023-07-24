import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager(path=r"C:\Users\user\PycharmProjects\pythonProject3").install())
    driver.maximize_window()
    yield driver
    driver.quit()

