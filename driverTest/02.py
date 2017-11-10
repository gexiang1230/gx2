#coding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)

#back练习
# driver.get('https://www.baidu.com/')
# driver.find_element_by_id('kw').send_keys(u'松勤\n')
# time.sleep(2)
# driver.back()      #返回前一个页面
# time.sleep(2)


#窗口的切换
driver.get(r'C:\Users\AJ002\PycharmProjects\gx2\driverTest\022.html')
print u'当前页面的标题 %s'%driver.title
ele = driver.find_element_by_tag_name('a').click()
# we=Select(driver.find_element_by_tag_name('a'))
# we.select_by_visible_text()
# curHandles = driver.current_window_handle
winHandles = driver.window_handles

for one in winHandles:
   driver.switch_to.window(one)
   print one.title
driver.back()
time.sleep(4)
print driver.title
time.sleep(5)
driver.forward()
print driver.title
time.sleep(5)
driver.refresh()


print driver.title





driver.quit()