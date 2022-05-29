import re


#使用match进行从头匹配

s='Learn Python' #定义评价字符串

mobj=re.match('Le',s)   #找到匹配，返回匹配部分
if mobj:
    print(mobj.group())

#不止是可以通过group取出匹配的字符
#还可以从匹配对象中取出一个范围

print(mobj.start()) #返回匹配位置的开头下标
print(mobj.end())   #返回匹配位置结尾的下标+1
print(mobj.span())  #返回（开头下标，结尾下标+1）

#找不到匹配，返回None
mobj=re.match('e',s)    
if mobj:
    print(mobj.group())
else:
    print(mobj)

#使用search进行中途匹配,可以从任意位置匹配
s='arararar'
mobj=re.search('ar',s)   
if mobj:
    print(mobj.group())




#通过制作好了进行模式转译的正则表达对象来实现快速匹配

s='1222 2323'
reobj=re.compile('12')
mobj=reobj.match(s)
if mobj:
    print(mobj.group())

#传入re.IGNORECASE参数进行忽略大小写的匹配
s="Water"
print("有转译时")
print("不忽略大小写：")
reobj=re.compile('wa')
mobj=reobj.match(s)
if mobj:
    print(mobj.group())
print("忽略大小写：")
reobj=re.compile('wa',re.IGNORECASE)
mobj=reobj.match(s)
if mobj:
    print(mobj.group())

print("无转译时")
print("不忽略大小写：")
mobj=re.match(s,'wa')
if mobj:
    print(mobj.group())
print("忽略大小写：")
mobj=re.match('wa',s,re.IGNORECASE)
if mobj:
    print(mobj.group())






#
print("正则表达式的个人尝试")

#判断一个字符串是不是1，2,3中任何一个的组合
s='21232'
sr='[123]*'
#直接匹配
mobj=re.match(sr,s)
if mobj:
    print(mobj.group())


#使用制作好了进行模式转译的正则表达对象来实现
reobj=re.compile(sr)
mobj=reobj.match(s)
if mobj:
    print(mobj.group())

