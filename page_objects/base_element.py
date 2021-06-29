from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()
    
    def clear(self):
        self.web_element.clear()

    def find(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None
    
    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
    
    @property
    def tyype(self):
        typpe=self.web_element.type
        return typpe


class Image(BaseElement):

    def download(self,path,keyword,i):        
        src=self.web_element.get_attribute('src') 
        urllib.request.urlretrieve(src, path+keyword+str(i)+'.png')
        return None
    
    def getInfo(self):
        return self.web_element.get_attribute('alt')


class Cast(BaseElement):
    def find(self):
        element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_all_elements_located(locator=self.locator)
        )
        self.web_element = element
        return None
    
    def getCastList(self):
        cast=self.web_element[0].text
        return cast.split("\n")
