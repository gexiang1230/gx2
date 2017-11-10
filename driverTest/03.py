# coding=utf-8
from selenium import webdriver
import time

executable_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get(r'C:\Users\AJ002\PycharmProjects\gx2\driverTest\022.html')

# 点击连接，打开新的窗口
link = driver.find_element_by_tag_name("a")
link.click()

# 显示 标题栏 文本，可以发现还是在当前网页
print driver.title

#保存主窗口handle
mainWindow = driver.current_window_handle

print driver.window_handles

for handle in driver.window_handles:
    # 切换到新窗口
    driver.switch_to.window(handle)
    # 检查是否是我们要进入的window
    if u'百度' in driver.title:
        break


kw = driver.find_element_by_id("kw")
kw.send_keys(u'松勤\n')

time.sleep(2)
driver.close()


#切换到主窗口
driver.switch_to.window(mainWindow)
driver.find_element_by_tag_name("input").send_keys('hello world')

raw_input('press any key to quit...')
driver.quit()