# coding:utf-8
from selenium import webdriver
from cfg import *


class WebOp (object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    cur_wd = webdriver.Chrome()
    cur_wd.get(LoginUrl )

    def TearBrower(self):
        self.cur_wd.quit()





