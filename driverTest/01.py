#coding: utf-8
from selenium import webdriver
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)
driver.implicitly_wait(10)   #找不到元素的时候会执行等待
driver.get('https://www.baidu.com/')
print driver.title
driver.find_element_by_id('kw').send_keys(u'松勤\n')
driver.find_element_by_id('1')
print driver.title            #获取当前窗口的title
# print driver.current_url        #获取当前窗口的地址
# driver.get_screenshot_as_file('s1.png')  #获取截图
mainWindows=driver.current_window_handle
#返回窗口的做法：方法1：修改循环中的title的名称  方法2：保存主窗口，切换的时候driver.current_window_handle（保存的窗口的名字）
driver.quit()