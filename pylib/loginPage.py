from selenium import webdriver
from coment.base import BasePage
from selenium.webdriver.common.by import By
import time
class loginpage(BasePage):
   url="http://10.10.64.38/#/login?componentInfo=400000053%2F705301000&uid=100000018"
   username=(By.CSS_SELECTOR,"input[type='text']")
   password=(By.CSS_SELECTOR,'input[placeholder="密"]')
   submit=(By.CSS_SELECTOR,"button[type='submit']")
   def login(self,username,password):
       self.getUrl(self.url)
       self.send_key(self.username,username)
       self.send_key(self.password,password)
       self.clik(self.submit)
       time.sleep(1)


if __name__=="__main__":
    dr=webdriver.Chrome()
    one=loginpage(dr)
    one.login("zy001","Tong#1234")


