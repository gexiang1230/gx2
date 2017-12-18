#coding:utf-8
from selenium import webdriver
import traceback
import WebOpAdmin
from cfg import *

class SearchInfo(WebOpAdmin.Login):
    ROBOT_LIBRARY_SCOPE='GLOBAL'
    def checkTextBox(self,locator):
        '''检查文本'''#当RF中使用这个类方法的时候会

        self.cur_wd.implicitly_wait(5)
        realx=self.cur_wd.find_element_by_css_selector(locator).text
        return realx


def checkSelectBox(self):
        pass

if __name__=='__main__':
    c=SearchInfo()
    c.login('ly','ly123!@#')
    print  c.checkTextBox()
    c.TearBrower()