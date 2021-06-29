from pytest import fixture
from selenium import webdriver

@fixture(scope='session')
def chrome_driver():
    browser = webdriver.Chrome('/Users/yihongli/Downloads/chromedriver')
    browser.maximize_window()
    yield browser