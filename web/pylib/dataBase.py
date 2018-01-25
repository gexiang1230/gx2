#coding:utf-8

import mysql.connector
import time
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8") #更改默认编码为utf-8
class dataPerform():
 #连接数据库-得到连接对象
    def __init__(self):
      self.con=mysql.connector.connect(
                        host='192.168.0.107',
                        port='9510',user='root',
                        password='Ebh123!@#',
                        database='cloud',
                        charset='utf8'
                        )


      self.cur = self.con.cursor()
    def querys(self,quertText):

      self.cur.execute(quertText)
      results=self.cur.fetchall()#取出全部数据
      self.cur.close()  # 关闭指针对象
      self.con.close()  # 关闭连接对象
      # result=str(results).replace('u\'','\'').decode('unicode-escape')
      for one in results:
          res=str(one).split(',')[0].split('(')[1]
          return res


if  __name__=='__main__':
   d=dataPerform()
   #查
   query = ("SELECT COUNT(DISTINCT cust_name) FROM db_main_list  WHERE  cust_name LIKE '李艳%'")
   result=d.querys(query)
   print result

