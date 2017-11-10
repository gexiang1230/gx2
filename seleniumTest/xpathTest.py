#coding:utf-8
from selenium import webdriver
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)
driver.get(u'file:///C:/%E5%AD%A6%E4%B9%A0/html/s1.html')
# eles=driver.find_elements_by_xpath('//div/*')
eles=driver.find_elements_by_xpath('//div[@id="food"]/*[last()-5]')
# eles=driver.find_elements_by_css_selector('p[spec*="len"]')
for ele in eles:
    print ele.get_attribute('outerHTML')
driver.quit()