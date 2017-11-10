import requests
import threading
url=['http://mirrors.163.com/centos/build/rpmcompare5.pl.txt',
     'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt'
    ]
#占位子
fileContent = [None for one in url]
#创建锁对象
lock=threading.Lock()
def childThread(idx,url):
    print '第%s个线程开始',idx
#获取网站内容


