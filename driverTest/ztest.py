#coding:utf-8
from selenium import  webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)   #找不到元素的时候会执行等待
driver.get('http://localhost/mgr/ps/mgr/index.html#/training')
# 选择培训班
driver.find_element_by_css_selector('[ui-sref="training"]')
#点击添加培训班
driver.find_element_by_css_selector('[ng-click*="showAddOne"]').click()
#填写培训班信息
driver.find_element_by_css_selector('[ng-model="addEditData.name"]').send_keys('java')
driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').send_keys('1')
driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').send_keys('1')
#选择课程
courses=driver.find_element_by_css_selector('[ng-model="$parent.courseSelected"]')
Select(courses).select_by_visible_text('数学')
driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
Select(courses).select_by_visible_text('语文')
driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
sleep(1)
#点击确认
driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
#验证结果

# driver.quit()