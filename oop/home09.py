# coding:utf-8
from random import randint  #随机产生选择
import time
class  Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal
class Tiger():
    classname='tiger'
    def __init__(self,weight):
        self.weight=weight
    def wows(self):
        print ("wow!!")
        self.weight -= 5
    def feed(self,food):
        if food=='meat':
            print("喂对了")
            self.weight+=10
        else:
            print ("喂错了")
            self.weight-=10
class Sheep():
    classname = 'sheep'
    def __init__(self,weight):
        self.weight=weight
    def wows(self):
        print ("mie~~")
        self.weight -= 5
    def feed(self,food):
        if food=='grass':
            print("喂对了,体重加10")
            self.weight+=10
        else:
            print ("喂错了,体重减10")
            self.weight-=10


rooms = []
for one in range(10):
    if randint(0,1):#产生动物
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(one,ani)#把动物放进房间里面
    rooms.append(room)
#游戏规则
starTime = time.time()
while True:
    endTime = time.time()
    if (endTime-starTime)>10:
         print("************游戏结束**********")
         for idx,room in enumerate(rooms):
           print('房间：%s,% (idx+1)', room.animal.classname, room.animal.weight)
           break
    roomo = randint(1,10)
    room=rooms[roomo-1]
    ch = raw_input('我们来到了%s，要敲门吗？[y/n]' % roomo)
    if ch == 'y':
        room.animal.wows()
    food = raw_input('请给房间里面的动物喂食:')
    room.animal.feed(food.strip())









