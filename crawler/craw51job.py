#coding:utf-8
from selenium import webdriver
import csv
# 要求如下：年新30万以上的岗位，
# 需要有招聘职位
# 需要有招聘内容
# 需要有招聘名称
exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(exepath)
driver.implicitly_wait(5)
driver.get('http://www.51job.com/')
# driver.find_element_by_id('kwdselectid1').clear()
driver.find_element_by_xpath('//div[@class="ush top_wrap"]//button').click()
#这里如果用了elements,表示结果是列表，不能有click方法
# jobinfo='\jobInfo.csv'
jobInfo =driver.find_element_by_id("resultList")#如果要用老师的层层选取的方法，不能出现List
allJobInfo=jobInfo.find_elements_by_class_name('el')
response_dicts=[]
for sinJobInfo in allJobInfo:
    response_dicts.append(sinJobInfo.text+',')
with open('\\jobInfo.csv','wb') as f:
    writer=csv.writer(f)
    writer.writerow(['职位名','公司名','工作地点','薪资','发布时间']) # 直接写表头 文件对象.writerow
    for repo_dict in response_dicts[1:]:
        writer.writerow(response_dicts)
driver.quit()

