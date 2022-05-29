#元组特性：不可添加，不可删除，不可变更

#元祖的定义方法


#可以直接使用括号包含一组逗号间隔的值来定义
#python元组支持包含重复元素
a=('a',123,"nihao",123)

print(a)
print(len(a))


#使用index可以获取元组中指定元素的下标
print(a.index('a'))
#可以指定index搜索指定下标的位置
print(a.index(123,1,4))
print(a.index(123,2,4))

#使用count计算元组里面指定元素的数量
print(a.count(123))


#可以将元组和元组连结，并重新定义一个元组
b=(1,2)
b+=a
print(b)
b=b+b
print(b)






