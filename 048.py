import re

#使用re.sub进行替换
s='Learn Python'
sa=re.sub('.n','gg',s)
print(sa)

#使用re.split进行分割

#把s由a,o,空格分割
slist=re.split('[ao ]',s)
print(slist)