

a=[1,2,3]
print(a)

#列表中添加元素
#添加到末尾，使用append
a.append(4)
print(a)

#添加到指定位置，使用insert
# a.insert(5,'maomao')    #如果插入越过末界，则会插入到末尾
a.insert(-100,"猫猫")   #如果插入的下标超过-3，则都按照-4处理（也就是说负下标不可超过最左点）
print(a)

#列表的连结,使用+关键字
b=['ni','hao','yjh']
c=a+b
print(c)

#也可以使用+=或者extend来实现列表联结，
#这两种方式，列表不会保留
b+=a    #原有的b列表被覆写
print(b)
b.extend(a)
print(b)

