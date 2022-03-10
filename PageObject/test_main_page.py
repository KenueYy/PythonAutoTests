from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()