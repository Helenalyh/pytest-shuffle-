from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_element import Image
from .base_page import BasePage
from .locator import Locator

class GooglePage(BasePage):

    url = 'http://www.google.com'

    def goto(self,substr):
        locator = Locator(by=By.PARTIAL_LINK_TEXT,value=substr)
        return BaseElement(driver=self.driver,
                            locator=locator)

    def findImage(self,i):
        self.imageButton.click()
        locator = Locator(by=By.XPATH,value='//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
        return Image(driver=self.driver,
                    locator=locator)
    
    @property
    def searchBar(self):
        locator = Locator(by=By.NAME, value='q')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    
    @property
    def imageButton(self):
        locator = Locator(by=By.XPATH, value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    
    def quit(self):
        self.driver.quit()
    
