#coding:utf-8
from selenium import webdriver
import traceback
import WebOpAdmin
from cfg import *

class SearchInfo(WebOpAdmin.Login):
    '''
    检查查询功能中的文本
    1.核实所有的文本
    2.核实所有文本框的内容
    3.查询后的字段
    '''
    ROBOT_LIBRARY_SCOPE='GLOBAL'
    def checkInfo(self):
        try:
          WebOpAdmin.Login.login(cdf.loginAdmin['name'],cfg.loginAdmin['pwd'])
          getAllInfo=self.cur_wd.find_element_by_id('formSearch')
          getAllInfoList=getAllInfo.get_attribute('innerTEXT')
          return  getAllInfoList
        except:
          print traceback.format_exc()


if __name__=='__main__':
    c=SearchInfo()
    print c.checkInfo