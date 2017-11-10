#coding:utf-8
import time
# MemTotal:        1016164 kB
# MemFree:          613420 kB
# MemAvailable:     812056 kB
# Buffers:           40928 kB
# Cached:           272128 kB
def GetContent(line,fild):
    for one in line:
        if fild in one:
            value = one.split(';')[1].split('kB')[0].strip()
            return int(value)
count = 0
while True:
    count += 1
    with open('/proc/meminfo') as f:
        begin=f.readlines()[:5]
        memfree=GetContent(begin,'MemFree')
        buffer=GetContent(begin,'Buffers')
        cache=GetContent(begin,'Cached')
        memtotal=GetContent(begin,'MemTotal')
        memUse=(memfree+buffer+cache)*100/memtotal
        menusage='%s         %.2f%%'%(time.strftime('%Y%M%D_%H:%M:%S'),memUse)

    with open('ret.txt','a') as f1:
        f1.write(menusage+'\n')
    if count>15:
        break



