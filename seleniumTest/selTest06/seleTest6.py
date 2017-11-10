#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
expath=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
url='https://www.vmall.com/'
#coding:utf-8
'''存储验证的字段'''
busWebMeunList= u'智能手机|笔记本&平板|穿戴设备|智能家居|更多产品|软件应用|服务与支持|华为商城'

appliWebMeunList= u'''首页|游戏|软件|专题|品牌专区|华为软件专区'''

officeWebMeunList=u'''平板电脑|笔记本电脑|笔记本配件'''

driver=webdriver.Chrome(expath)
driver.implicitly_wait(10)
#获得起始网站
driver.get(url)
#找两个点击的地址
#1.点击华为官网
driver.find_element_by_css_selector('.s-sub li:nth-child(1)').click()
#2.点击应用商场,先鼠标悬停后，再找元素

eleMenu=driver.find_element_by_css_selector('.icon-dropdown')
eleSin=driver.find_element_by_css_selector('.dropdown-more dt:nth-of-type(2) a')
ActionChains(driver).move_to_element(eleMenu).click(eleSin).perform()
#3.验证打开的句柄是否正确
allHandles=driver.window_handles

for handles in allHandles:
   driver.switch_to.window(handles)
#执行华为应用商场的操作
# xpath的定位语句：//*[@class="menu menu_cn"]//li
   if driver.title==u'华为消费者业务官网-华为智能手机|HUAWEI Mate 10':
      busWebMeun1=driver.find_elements_by_css_selector('.menu.menu_cn li a')
      eleText1=[one.text for one in busWebMeun1]
      actual1='|'.join(eleText1)
      if actual1 == busWebMeunList:
         print('bus page pass')
      else:
         print('bus page fail!!!!')


#执行华为消费者业务官网的操作
   if driver.title==u'华为应用市场 - 华为官方安卓市场':
       appliWebMeun2=driver.find_elements_by_css_selector('.ul-nav.emo_nv.cl li a')
       eleText2 = [one.text for one in appliWebMeun2]
       actual2 = '|'.join(eleText2)
       if actual2 == appliWebMeunList:
           print('app page pass')
       else:
           print('app page fail!!!!')
# if driver.title==u''
   if driver.title==u'华为商城官网-华为Mate10、华为P10、荣耀9、荣耀畅玩7X、' \
                    u'麦芒6、华为Mate9、荣耀V9、华为nova2官方网站':
       menu3=driver.find_element_by_css_selector('#zxnav_1 .category-info')
       #.subcate-list.clearfix
       ActionChains(driver).move_to_element(menu3).perform()
       meunList = driver.find_elements_by_css_selector('#zxnav_1 .subcate-list.clearfix span')#这一句定位有做错了
       actual31=[ one.text for one in meunList]
       actual3='|'.join(actual31)
       if actual3==officeWebMeunList:
           print 'office is pass!'
       else:
           print  'office is false!!'

#获得两个地址的菜单

#验证是否正确,用上截图功能

#跳回原来的窗口，验证笔记本电脑菜单
driver.quit()