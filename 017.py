#列表排序
#sort方式
a=[1,4,3,2,5]
a.sort()    #默认升序排列
print(a)
a.sort(reverse=True)     #指定参数进行降序排列
print(a)

#使用sorted生成新列表（排好序的），保留旧列表
b=sorted(a)
print(b)

b=sorted(a,reverse=True)
print(b)






