# coding:utf-8
from selenium import webdriver
import time,traceback
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platforVersion'] ='7.0'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'C:\tools\apk\com.ibox.calculators_2.8.5_585.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote(r'http://localhost:4723/wd/hub',desired_caps)

try:
    driver.implicitly_wait(3)
    time.sleep(3)
    driver.find_element_by_id('com.ibox.calculators:id/digit3').click()#3
    driver.find_element_by_id('com.ibox.calculators:id/plus').click()#+
    driver.find_element_by_id('com.ibox.calculators:id/digit9').click()#9
    driver.find_element_by_id('com.ibox.calculators:id/equal').click()#=
    driver.find_element_by_id('com.ibox.calculators:id/mul').click()#*
    driver.find_element_by_id('com.ibox.calculators:id/digit5').click()#5
    driver.find_element_by_id('com.ibox.calculators:id/equal').click()#=

    out1=driver.find_element_by_id('com.ibox.calculators:id/cv')#找父节点的唯一id
    out2=out1.find_elements_by_class_name('android.widget.TextView')
    out=out2[1].text
    print out
    if out=='60':
        print 'pass'
    else:
        print 'failed'







except:
    print traceback.format_exc()







