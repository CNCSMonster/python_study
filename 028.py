# for提取列表中的值

a=[1,4,3]

for mi in a:        #使用for访问列表中的值也是顺序的
    print(mi)


b=(1,24,4)              #使用for打印元组得到的值是顺序的
for mb in b:
    print(mb)


#使用for-else语句
w={'星期五','星期六','星期天'}      #使用for语句遍历集合打印出来的结果是乱序的
for wday in w:      
    print(wday)
else:       #else接的模块将在循环结束后执行
    print("是周末")


#使用for提取字典的指定内容
w={'星期五':5,'星期六':6,'星期天':7}

for keys in w:      #默认情况下表示取字典中的键
    print(keys)

for val in w.values():
    print(val)

for item in w.items():
    print(item)


#问题,for语句访问列表并修改真的修改了列表的值吗

#对整数等基础数据类型无法真正修改列表值
a=[1,2,3,5]
for x in a:
    x+=1

print(a)

#对字符串类型也不能
a=['ad adfa','dssd']
for x in a:
    if type(x)==str:
        x.replace('a','b')
print(a)


#对列表类型可以
a=[[1,2],[23,33]]
for x in a:
    x.pop(0)
print(a)

#对字典可以
a=[{'a':1,'b':2},{'s':1,'g':12}]
print(a)
for x in a:
    key=list(x.keys())
    x.pop(key[0])

print(a)










