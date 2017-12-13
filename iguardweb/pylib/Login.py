#coding:utf-8
from selenium import webdriver

import  time
class Login:
    def OpenBrower(self):
        self.cur=webdriver.Chrome()
    def login(self):
        self.cur.find_element_by_id()
