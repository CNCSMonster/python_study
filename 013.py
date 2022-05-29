#列表的几种生成方法
a=[1,2,3]
animal_list=list()
animal_listb=[]

#不同数据类型的值可以保存在同一个列表中
a=['猫',100,23.33]

#列表中元素的访问
print(a[0])
print(a[-1])

#更新列表中元素的值
a[0]="one"
a[1]='second'
a[2]='third'
print(a)

# 思考题：元组可以是列表的元素吗？
b=(1,32,4)
a[0]=b
print(a)

#列表可以是列表的元素吗
c=[12,32,24]
a[0]=c
print(a)


#列表中的元素可以重复出现吗
list=list()
list.insert(0,1)
list.insert(1,3)
list.append(3)
print(list)
