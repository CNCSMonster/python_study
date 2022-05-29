
a=[1,'2',4,3,'2']
print(a)

#删除列表中的元素
#根据序号删除
b=a.pop(2)
print(b)
print(a)
#根据值来删除
c=a.remove('2') #会删去列表中从前到后遇到的第一个该值元素
print(a)
print(c)    #当列表中有想要删去的值，返回结果为None
# c=a.remove('nihao')   #如果列表中没有想要删去的值，会返回错误信息


#也可以通过del命令进行删除
#该操作时把元素的对象本身从内存中删去
del a[1]
print(a)    


#将列表分割为变量
a=['ni','hao','a']
a,b,c=a
print(a,b,c)


