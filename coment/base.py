from  selenium import webdriver
import time

def browser(type_):
    try:
        return getattr(webdriver,type_)()
    except:
        return webdriver.Chrome()

class BasePage:

    webdriver.Chrome.quit()
    def __init__(self,driver):
        self.driver=driver
    def loctor(self,loc):
        return self.driver.find_element(*loc)
    def send_key(self,loc,value):
         self.loctor(loc).send_keys(value)
    def getUrl(self,url):
        self.driver.get(url)
    def clik(self,loc):
        self.loctor(loc).click()
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()

if __name__=="__main__":
    driv=webdriver.Chrome()
    one=BasePage(driv)
    url="http://10.10.64.38/#/login?componentInfo=400000053%2F705301000&uid=100000018"
    one.getUrl(url)
    time.sleep(3)
    one.driver.close()