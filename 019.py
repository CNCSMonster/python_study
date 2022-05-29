#python里面的字典是花括号括起来的一系列键值对的形式
#键可以是任何基本数据类型，还可以是字符串、元组，但是不能是列表
#键值对的书写格式：  键:值

#字典的定义方法
a={"你好":1,"you":2,"why":3}

b={(1,2):3,(3,4):7,(5,6):11}

# c={[1,2]:1,[3,4]:2}   #列表不能作为字典的键

print(a,b,sep='\n')

#引用字典中的元素

V1=a["你好"]
V2=b[(1,2)]
print(V1,V2)


#使用in或者not in运算符来查询是否存在键
c='cao' in a
print(c)
print('nimen' not in b)

#使用get()方式，如果存在则返回指定键对应的值，如果不存在，则返回None

V1=a.get('你好')
Vb=a.get('fu')
print(V1,Vb)




