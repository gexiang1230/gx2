#coding:utf-8
from selenium import webdriver
from pylib import WebOp
class MenuPersom(WebOp.WebOp):#继承的时候是模块名加类名，即使两个名字相同也要写
    '''用于选择菜单'''
    # #navbar   .nav-item.open
    # //ul[@id="navbar"]/ li[8]//span[1]
    ROBOT_LIBRARY_SCOPE='GLOBAL'
    # ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def simImport(self):
        '''选择sim卡管理菜单'''
        self.cur_wd.implicitly_wait(10)  # 隐式等待是等待5秒，页面加载完毕后获取元素
        self.cur_wd.maximize_window()
        self.cur_wd.refresh()

        self.cur_wd.find_element_by_xpath('//ul[@id="navbar"]/li[3]/a//span[1]').click()
        sleep(2)
        self.cur_wd.find_element_by_xpath('//*[@id="navbar"]/li[3]//i[@class="icon-users"]/../span').click()






