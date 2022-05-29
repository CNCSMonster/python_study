#往字典中添加元素，两种方法：直接定义法，setdefault法
a=dict()
print(a)
a["nihao"]=1
print(a)
a.setdefault('你们',2)#使用setdefault方法可以不能覆写字典中已经存在的键对应的值
print(a)

#删除字典中的元素，两种方法：del命令或者pop方式或者clear方法

c=a.pop('nihao')
print("what was pop out is:",c)
print(a)



del a['你们']
print(a)

a[44]=5
print(a)

#使用clear
a.clear()
print(a)




