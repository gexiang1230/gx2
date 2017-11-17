# coding:utf-8
from appium import webdriver
import traceback,time

desire_caps={}
desire_caps['platformName'] = 'Android'
desire_caps['platformVersion'] = '7.0'
desire_caps['deviceName'] = 'test'
desire_caps['app'] = r'C:\tools\apk\toutiao.apk'
desire_caps['appPackage'] = 'io.manong.developerdaily'
# C:\Users\AJ002\AppData\Local\Android\sdk\build-tools\25.0.3
desire_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desire_caps['unicodeKeyboard'] = True
desire_caps['noReset'] = True
desire_caps['newCommandTimeout'] = 6000 #测试程序链接appium sever 成功之后，等待客户端发动命令，当中间有段时间没有发命令的时候，一直保持通信的时间6000后，就可以链接断开

driver=webdriver.Remote(r'http://localhost:4723/wd/hub',desire_caps)
try:
    driver.implicitly_wait(3)
    driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_plus').click()

    time.sleep(2)
    driver.find_element_by_id('io.manong.developerdaily:id/btn_email').click()


    driver.find_element_by_id('io.manong.developerdaily:id/edt_email').send_keys('jcyrss@163.com')
    driver.find_element_by_id('io.manong.developerdaily:id/edt_password').send_keys('sdfsdf')
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()

except:
    print traceback.format_exc()