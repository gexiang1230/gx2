#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)
driver.get(r'https://kyfw.12306.cn/otn/leftTicket/init')
#输入起始地点
origin =driver.find_element_by_id('fromStationText')
origin.click()
origin.clear()
origin.send_keys(u'南京南\r\n')

#输入目的地
desti=driver.find_element_by_id('toStationText')
desti.click()
desti.clear()
desti.send_keys(u'杭州东\r\n')
#选择日期
driver.find_element_by_css_selector('#date_range li:nth-of-type(2)').click()
#选择时间
Select(driver.find_element_by_id('cc_start_time')).select_by_index('2')

# 方法1  css定位
# allTrain=driver.find_elements_by_css_selector('#queryLeftTable > tr')
# # print allTrain
# # allTrainTime=allTrain.find_elements_by_css_selector('[id^="ZE"]')
# # driver.implicitly_wait(3)
# # for alltraintime in allTrainTime:
# #     print alltraintime.text
# #
# for one in allTrain:
#     trains=one.find_elements_by_css_selector('[id^="ZE"] ')
#     if trains:
#         trainss=one.find_element_by_css_selector('td:nth-child(1) .train a')
#         print trainss.text
#xapth = '//*[@id="queryLeftTable"]//tr[@class]//td[4][@class]/../td[1]//div[@class="train"]//a'
trains=driver.find_elements_by_xpath('//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a')
time.sleep(10)
print trains
print(len(trains))
for train in trains:
    tr=train.text
    print tr

driver.quit()








