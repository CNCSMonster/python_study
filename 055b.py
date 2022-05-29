from asyncio.windows_events import NULL
from datetime import datetime as dt
import sys
from warnings import catch_warnings
from xmlrpc.client import boolean
fn="time.txt"
def appendTime(gowork):
    if(type(gowork)!=boolean):
        print("输入的参数不是布尔逻辑值")
    now=dt.now()    #获取现在时刻
    mode='上班'if gowork else '下班'
    s=f'{mode} {now.year}-{now.day}-{now.hour}:{now.minute}'
    print(s)
    with open(fn,'a') as fs:
        fs.write(s+'\n')

def ListTime():
    try:
        with open(fn,'r') as fr:
            for r in fr:
                print(r)
    except:
        print("文件无法读取")

if len(sys.argv)>1 and sys.argv[1]=='i':
    appendTime(True)
elif len(sys.argv)>1 and sys.argv[1]=='o':
    appendTime(False)
else:
    ListTime()

