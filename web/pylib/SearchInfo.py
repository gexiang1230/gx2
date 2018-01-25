#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import traceback
import WebOpAdmin
from cfg import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By
from    time  import sleep
import os


import sys
reload(sys)
sys.setdefaultencoding("utf-8") #更改默认编码为utf-8

class SearchInfo(WebOpAdmin.Login):
    ROBOT_LIBRARY_SCOPE='GLOBAL'
    def checkTextBox(self,locator):
        '''检查文本'''#当RF中使用这个类方法的时候会
        self.cur_wd.implicitly_wait(5)
        realx=self.cur_wd.find_element_by_css_selector(locator).text
        return realx



    def checkSelectBox(self,frameName,**argv):
        '''各种查询的文本框'''
        self.cur_wd.implicitly_wait(5)
        if frameName==u'姓名':
           self.cur_wd.find_element_by_id('custName').send_keys(argv['inputs'])
        if frameName==u'电话':
            self.cur_wd.find_element_by_id('custPhone').send_keys(argv['inputs'])
        if frameName==u'设备':
            pass
        if  frameName==u'等级':
            pass
        if  frameName==u'慢病阶段':
            stage=Select(self.cur_wd.find_element_by_id('cdStage'))
            stage.select_by_visible_text(argv)
        if  frameName==u'设备号':
            self.cur_wd.find_element_by_id('devCode').send_keys(argv['inputs'])
        if  frameName==u'未测天数':
            self.cur_wd.find_element_by_id('mNoDays').send_keys(argv['inputs'])
        if  frameName==u'联系方式':
            link=Select(self.cur_wd.find_element_by_id('link'))
            link.select_by_index(ind)
        if  frameName==u'所属客服':
            customerSever=Select(self.cur_wd.find_element_by_id('userId'))
            customerSever.select_by_visible_text(customer)
        if   frameName==u'订单号':
            self.cur_wd.find_element_by_id('orderId').send_keys(argv['inputs'])
        if   frameName==u'客户编号':
            self.cur_wd.find_element_by_id('custNumber').send_keys(argv['inputs'])
        if   frameName==u'未回访':
            noReturn=Select(self.cur_wd.find_element_by_id('rvNeverDays'))
            noReturn.select_by_visible_text(link)
        if   frameName==u'到期时间':
            dueTime=Select(self.cur_wd.find_elements_by_class_name('simDueNum'))
            dueTime.select_by_index(dueTimeIndex)
        if   frameName==u'用户组别':
            self.cur_wd.find_element_by_id('selectParent').click()
            self.cur_wd.find_element_by_id(groupId).click()#'groupTree_1_span'
    def search(self):
        self.cur_wd.implicitly_wait(5)
        login = self.cur_wd.find_element_by_xpath\
         ('//*[@class="col-sm-2"]//button[@type="button"]').click()

        for i in range(1,999):
            # self.cur_wd.implicitly_wait(20)
            #临时增加等价的时间，在20s内一直等待页面加载完成
            #代码中可以使用显示等待，增加代码的健壮性
           locator=(By.CSS_SELECTOR,'#dataList  tbody  tr')
           WebDriverWait(self.cur_wd,10,0.5).until(EC.presence_of_element_located(locator))
           allList = self.cur_wd.find_elements_by_css_selector('#dataList  tbody  tr')

        # allTexts=[one.text.split(' ')[0]  for one in allList]
        # #解决代码的Unicode转换
        # a = str(allTexts).replace('u\'', '\'')
        # names = a[0].decode("unicode-escape")
        return allList[0].text


    def  loading(self):
        '''首页搜索功能'''
        self.cur_wd.implicitly_wait(3)
        login=self.cur_wd.find_element_by_xpath\
                ('//*[@class="col-sm-2"]//button[@type="button"]').click()
        # 窗口冻格后检查-正在加载
        # 对于这种逻辑:出现一段时间就消失的文本或者内容，可以使用循环去捕捉，捕捉到就返回退出
        # 如果没有这么做会发生不可解释的现象
        sleep(3)

        resultNumbers = self.cur_wd.find_element_by_css_selector('.portlet.light   .pagination-info')

        if resultNumbers:
            testString=str(resultNumbers.text).split('，')[1]

            return   testString

        else:
            for i in range(1,99):
              loadingText= self.cur_wd.find_element_by_xpath('//*[@id="dataList"]/../div').text
              if  loadingText:
                  return loadingText

    def  SimImportPerform(self,perfrom):
         '''导入SIM卡操作
         perfrom:
         1.导入文件
         2.下载文件
         '''
         # self.cur_wd.implicitly_wait(10)  # 隐式等待是等待5秒，页面加载完毕后获取元素
         # self.cur_wd.maximize_window()
         # self.cur_wd.refresh()
         #
         # self.cur_wd.find_element_by_xpath('//ul[@id="navbar"]/li[3]/a//span[1]').click()
         # sleep(2)
         # self.cur_wd.find_element_by_xpath('//*[@id="navbar"]/li[3]//i[@class="icon-users"]/../span').click()
         sleep(2)
         if perfrom==1:
             #---这里新打开了页面，handles需要重定向
             self.cur_wd.switch_to.window(self.cur_wd.window_handles[-1])
             sleep(2)
             self.cur_wd.find_element_by_id('photoCover').click()
             os.system(r'C:\Users\AJ002\Desktop\12.exe')
             self.cur_wd.find_element_by_css_selector('[onclick*="doImport"]').click()

         else :
             self.cur_wd.find_element_by_css_selector('[onclick*="downloadTemplate"]').click()










if __name__=='__main__':
    c=SearchInfo()
    c.login('ly','ly123!@#')

    c.SimImportPerform(1)
    c.TearBrower()