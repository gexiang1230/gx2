#coding:utf-8
from selenium import webdriver
import time
expath=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(expath)
driver.implicitly_wait(10)
driver.get('http://121866.com/cust/sign.html')
driver.find_element_by_id('username').send_keys('gx')
driver.find_element_by_id('password').send_keys('gx1234')
driver.find_element_by_id('btn_sign').click()
time.sleep(2)
#原来的第一个的标题
eleTest=driver.find_element_by_xpath('//*[@class="article-content"]/div').text
#编辑按钮
driver.find_element_by_xpath('//*[@class="article-content"]/div[1]/div[2]/i').click()
time.sleep(2)
twice=driver.find_element_by_xpath('//*[@id="title"]/input')
twice1=twice.get_attribute('value')
if twice1==eleTest:
    print 'yes'
else:
    print 'no'
print u'第二页'+twice1
print u'第一页'+eleTest

driver.quit()