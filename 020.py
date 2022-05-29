#字典中元素的值可以覆写
a={'a':1,'b':2}
print(a)
a['a']=3
print(a)

#利用dict()创建字典
d=dict(巧克力=1,年后好=2,你们是=3)
#使用dict()创建字典，里面的参数即使是字符串也不需要加引号
#里面等号格式的键值对为左键右值

#或者使用zip(),将键列表和值列表融合来创建字典
key=['ni','hao','yjh']
value=[1,2,3]
d=dict(zip(key,value))
print(zip(key,value))

#从元祖的列表中创建字典
d=dict([('nihao',1),('womenshi',2),('正义者联盟',3)])
print(d)









