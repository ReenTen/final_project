import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_browser():
    with allure.step('Initializing chromedriver manager'):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(5)
        yield browser
    with allure.step('Closing browser'):
        browser.quit()