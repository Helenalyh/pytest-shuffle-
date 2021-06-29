from pytest import mark
from selenium import webdriver
from page_objects.google_page import GooglePage
from selenium.webdriver.common.keys import Keys

class TestGoogle():
    def setup_class(self):
        chrome_driver=webdriver.Chrome('/Users/yihongli/Downloads/chromedriver')
        self.webPage = GooglePage(driver=chrome_driver)
        self.webPage.go()
        print('set up')
        
    def teardown_class(self):
        print('tear down')
        for handle in self.webPage.driver.window_handles:
            self.webPage.driver.switch_to.window(handle)
            self.webPage.driver.close()
        self.webPage.quit()
    
    def teardown_method(self,method):
        self.webPage.searchBar.clear()
    
    def test_1(self):
        print('test order 1.1')
        self.webPage.searchBar.input_text('cauliflower')
        self.webPage.searchBar.input_text(Keys.ENTER)
        self.webPage.goto('wikipedia').click()

    def test_2(self):
        print('test order 1.2')
        self.webPage.searchBar.input_text('broccoli')
        self.webPage.searchBar.input_text(Keys.ENTER)
        self.webPage.goto('healthline').click()
    
    def test_3(self):
        print('test order 1.3')
        self.webPage.searchBar.input_text('spinach')
        self.webPage.searchBar.input_text(Keys.ENTER)
    

    def test_4(self):
        assert 1==1
        print('test order 2.4=')


    
    
