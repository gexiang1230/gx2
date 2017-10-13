from selenium import webdriver
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)
driver.get('https://www.vmall.com/')
eles = driver.find_elements_by_xpath('//div[@class="home-recommend-goods home-hot-goods"]//h3')
for ele in eles:
  print ele.text
driver.quit()