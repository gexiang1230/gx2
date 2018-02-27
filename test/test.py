#coding:utf-8
from decimal import *
import sys
#
# with localcontext() as t:
#      t1=getcontext()
#      t1.prec=2  #设置小数保留的位数
#      print  Decimal('1')/Decimal('3')   #0.33


# print  decimal.Decimal('1')/decimal.Decimal('3')   #0.3333333333333333333333333333

# x = set([1,2,3,4])
# print  x


#集合解析-花括号中
#print {x**2  for x in [1,2,3,4]}#set([16, 1, 4, 9])说明集合是无序的
#

# print list(set([1,2,2,3,4,6,6,6]))#set去重特性
#
#
# a='abcdefg'
# b='abcefg'
# print id(a),id(b)

#引用
# a=3
# b=3
# a=a+2
# c=['abc']
# d=c
# c[0]='d'
# print a,b,c,d

# import copy
# c=['abc']
# d=copy.copy(c)
# c[0]='d'
# print c,d##['d'] ['abc'],如果做了对象的拷贝，共享引用的是不会改变其他对象的值的

# a=[1,2,3,4]
# b=[1,2,3,4]
# print a is b  #is 比较对象的指针，==比较对象的值

# a=1
# b=1
# print a is b   # True,python中小数和整数是复用的，所以对象是相同的



# a="abc\a\""   #abc"
# # a='a\ta'
# print a
# # print '\\\\\\r'
# print '*'*80
#
# import re
# a=re.split(',|\|','a,b,c|d|e|f')
# print a+9

# a='abcdefg'#报错can only concatenate list (not "str") to list
# b=list(a)
# c='span'.join(b)
# print a+'\n',b,'\n',c


#格式化字符串
# print '%%%.2f%%'%(1/3.0)
# print ord('s')
# print chr(126)

#
# # print len([1,2,3,4])
# # a = ['1','2','3','4']
# a = [123, 'xyz', 'zara', 'abc']
# # a.reverse()#这个操作并没有返回值，reverse是直接对原来的列表进行操作，所以直接print a.reverse(),是返回none
# # print a.append('d')#同理None
# # print a  #此时a的值已经改变，所以返回['xyz', 'abc', 'zara', 'xyz', 123]
# # a.sort()
# # print a   #[123, 'abc', 'd', 'xyz', 'xyz', 'zara']
# # a.sort(reverse=True)
# # print a
# a.sort() #['zara', 'xyz', 'd', 'abc', 123]
# print a#['zara', 'xyz', 'd', 'abc', 123]



'''字典方法'''
# d={'spam':2,'ham':1,'egg':3}
# print list(d.values())
# print list(d.items())
# print d.get('12',12)
# print dict.fromkeys(['a','b'],0)#批量生成默认值的方法--{'a': 0, 'b': 0}
#
# print list(zip(['a','b','c'],[1,2,3])) #[('a', 1), ('b', 2), ('c', 3)]



# 文件--在文件中存储并解析python对象，其他非str对象的必须要将对象转换成字符串
#使用str工具转换
# X,Y,Z=43,44,45 #数字类型
# S='Spam'       #字符串类型
# D={'a':1,'b':2}#字典类型
# L=[1,2,3]      #列表
# F=open('datafile.txt','w+')
# F.write('%s%s%s'%(X,Y,Z))
# F.write(str(L)+'$'+str(D)+'\n')
# line=F.readline()
# print line.split('$')[0]
# F.close()


# g=[1,8,3]
# g1=['a',g,'b']
# g2={'x':g,'y':2}
# print sys.getrefcount(g)#调用sys.getrefcount()判断X对象被引用的次数,4次
# A=[1,2]
# b=1
# print sys.getrefcount([1,2])#直接写对象类型，就是1次而不是2次



# g=[1,8,3]
# g.append(g)
# print g  # [1, 8, 3, [...]]

# x = 1
# y = 2
# print '输出结果为{}{}'.format(x,y)

'''除法'''
# x=1
# y=3.0
# print x/y,x//y

'''none'''
# L=[None]*100
# print L

'''重定向输出流'''
#法1
# import sys
# tmp = sys.stdout
# sys.stdout = open('log.txt','a')
# print 'spam'
# tmp.close()#关闭
# sys.stdout=tmp
# print 'hahah'
#
# f2=open('f2.txt','a')
# # print ('x',file=log)#py3x的方法 流输出到文件中
# print >>f2,'x'#py2x，输出到文件中
# print 'y'  #标准输出流输出

# 疑问
# x = 1
# y = 2
# import sys
# sys.stdout.write(str(x)+' '+str(y)+'\n')



'''推选下一任群主'''
# import random
# print random.randint(1,5)

'''二维+一维组成三维数据'''
L1=[1,2,3,4]
L2=[[1,1],[2,2],[3,3],[4,4]]
for one in L2:
      one.append(L1[0])
      L1 = L1[1:]
      print one

# s = 'spam'
# for (x,y) in enumerate(s):
#     print x,',',y
