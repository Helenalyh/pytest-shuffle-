from pytest import mark
from selenium import webdriver


class Test():
    #@classmethod
    def setup_class(self):
        self.browser = webdriver.Chrome('/Users/yihongli/Downloads/chromedriver')
        self.browser.maximize_window()
        self.browser.get('http://www.google.com')
        print('set up 1')
        
        
    #@classmethod
    def teardown_class(self):
        print('tear down 1')
        self.browser.close()
        
    
    def test_1(self):
        assert 1==1
        print('test order 1.1')

    #@mark.run(order=orders[1])
    def test_2(self):
        assert 1==1
        print('test order 1.2')
    
    #@mark.run(order=orders[2])
    def test_3(self):
        assert 1==1
        print('test order 1.3')
    
    #@mark.run(order=orders[3])
    def test_4(self):
        assert 1==1
        assert 1==1
        print('test order 1.4')

    
    
