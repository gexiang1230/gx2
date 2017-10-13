from selenium import webdriver
import time
def deleteAllLesson():
  exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
  driver = webdriver.Chrome(exepath)
  driver.get('http://localhost/mgr/login/login.html')
  driver.find_element_by_id("username").send_keys('auto')
  driver.find_element_by_id("password").send_keys('qwe123')
  driver.find_element_by_css_selector('[class="btn btn-success"]').click()
  driver.implicitly_wait(4)
  while True:
     eles = driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
     print eles
     if eles:
         eles[0].click()
         driver.find_element_by_css_selector('button.btn-primary').click()
         time.sleep(1)
     else:
         break
  driver.quit()
