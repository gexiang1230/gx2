#coding:utf-8
# from selenium import webdriver
# exepath = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(exepath)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id("kw").send_keys(u'悠悠')
# driver.find_element_by_id("kw").submit()
# # driver.find_element_by_css_selector()
import itertools
def getmin(numbers):
    nlist=itertools.permutations(numbers,len(numbers))
    nlist2=[one for one in nlist]
    nlist3=[]
    for one in nlist2:
        new=[str(i) for i in one]
        nlist3.append(''.join(new))
    print nlist3
    return min(nlist3)
print getmin([3,32,321])