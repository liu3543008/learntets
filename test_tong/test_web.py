#coding=utf8
import request,re,pytest
from selenium import webdriver
from pylib.loginPage import loginpage
from coment.yaml_test import Yaml
from ddt import ddt,file_data

one = Yaml("../data.yaml")


print(one.yaml_load())
class Testweb:
    # def setup_class(self):
    #     self.driver=webdriver.Chrome()

    @pytest.mark.parametrize('up',one.yaml_load())
    def test_001(self,up,browser):
            nn=loginpage(browser)
            nn.login("zy001","Tong#1234")













