#与字典类似，集合定义时也是用花括号括住
#但是集合的元素只是单一的数据类型，
#而不是键值对
a={'a','b','c'}
b={(1,2),2,4}   #集合的元素可以是元组
print(a)
print(b)

#如何获得集合:通过其他数据类型转换
seta=set("abcsd")
setb=set([1,2,34,5])
#集合也可以转换为其他数据类型
list=list(setb)
print(seta,setb,list)


#获取集合中元素的个数
colorM={'c','M'}
print(len(colorM))

#使用in 来查询特定的值是否被包含于集合之中
a='nihao' in colorM
print(a)
a='c' in colorM
print(a)








