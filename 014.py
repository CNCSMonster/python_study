
#获得列表的长度，使用len函数
a=['猫',100,23.33]
print(len(a))
lenth=len(a)
print(type(lenth))

#使用in关键字来判断某个元素是否在列表中
chk = 'mao' in a
chkn = "猫" in a
print(chk)
print(chkn)

#从别的值转化为列表型,使用list函数
lista =list("nihao")
print(lista)
listb =list((2,3,4))
print(listb)

#列表中的列表
list =[lista,listb,a]
print(list)



