#coding:utf-8
from appium import webdriver
import time,traceback

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'
desired_caps['deviceName']='test'
desired_caps['app']=r'C:\tools\apk\com.ibox.calculators_2.8.5_585.apk'
desired_caps['appPackage']='com.ibox.calculators'
desired_caps['appActivity']='com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard']=True
desired_caps['noSet']=True
desired_caps['newCommandTimeout']=6000

driver=webdriver.Remote('http://localhost/wd/hub',desired_caps)
driver.find_elements_by_xpath('')