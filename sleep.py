#coding:utf-8
import datetime
'''睡眠'''
def inputime(startEndTime):
    '''时间转化为小时'''
    start = startEndTime.split('.')
    startMole = int(start[1]) / 60.0 + int(start[0])
    return startMole
def parameter_y(a):
    '''计算睡眠时长系数y'''
    if a>8:
        y=1-(a-8)/8.0
    elif a<6:
        y = 1 -(6-a) / 6.0
    else:
        y = 1
    return  y

def parameter_x(p1,p2,p3,p4,p5,p6):
    '''p1:入睡时间； P2:睡眠比例；  p3:REM比例;  p4:打鼾时长; p5:辗转次数/小时;p6：呼吸暂停'''
    x=100
    if p1<20 or p1>23:
        x -= (p1 - 23) / 0.5 * 4
    elif p2 < 10:
        x -= (10 - p2) / 2.0 * 4
    elif p3<20:
        x-=20-p3
    elif p4>=10:
        x-=(p4-10)/5.0*2
    elif p5>10:
        x-=(p5-10)*2.0
    elif 60<=p6<=120:
        x-=p6/6
    return x



if __name__=='__main__':

  # startime= raw_input('睡眠开始时间')
  # endtime=raw_input('睡眠结束时间')
  # p1=raw_input('p1:入睡时间')
  # p2= input('p2:深度睡眠的时间')
  # p3 =input('p3:REM睡眠时长')
  # p4 = raw_input('p4:打鼾时长')
  # p5 = raw_input('p5:辗转次数 / 小时')
  # p6 = raw_input('p6：呼吸暂停')
  # timeValue=inputime(endtime)-inputime(startime)
  # p22 = p2/timeValue
  # p33 = p3 / timeValue
  # y= parameter_y(timeValue)
  # x=parameter_x(p1,p22,p33,p4,p5,p6)
  # print x*y


  timeValue = inputime('6.05') - inputime('0.0')
  p22 = 0.57 / timeValue
  p33 = 1.73 / timeValue
  y = parameter_y(timeValue)
  print timeValue,y,p22,p33
  x = parameter_x(24, p22, p33, 16, 30, 60)
  print x
  print x * y

# 睡眠开始时间3.40
# 睡眠结束时间6.05
# p1:入睡时间27.67
# p2:深度睡眠的时间0.57
# p3:REM睡眠时长1.73
# p4:打鼾时长16
# p5:辗转次数 / 小时76
# p6：呼吸暂停60


