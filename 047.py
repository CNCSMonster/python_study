import re

#默认是最长匹配
mobj=re.match('L.*n','Learn Python')
if mobj:
    print(mobj.group())

#在表示不确定数量的特殊功能符号后面加？则设定为最短匹配
mobj=re.match('L.*?n','Learn Python')
if mobj:
    print(mobj.group())


#使用findall获得所欲匹配结果的一个列表
s='Learn Python,Learn math,Lgggn s'
mlist=re.findall('L.*n',s) #默认获得最长匹配的列表
print(mlist)
mlist=re.findall('L.*?n',s) #用？指定，获得最短匹配的列表
print(mlist)

#使用finditer获得所有符合的字符串的位置,或者说获得所有满足的匹配的列表
print("使用finditer")
s='in sun'
miter=re.finditer('.n',s)
print(miter)
for mobj in miter:
    print(mobj.group())
    print(mobj.span())


