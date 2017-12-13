#coding:utf-8
from oop import home
class Child(home.home):#继承的时候可以使用【模块名.类名】的方式继承
    def childMethod(self):
        print'调用子类方法'
        home.home.parentMethod(self)

if __name__ =='__main__':
   c = Child()
   c.childMethod()