#一种使用yield处理的生成器函数

#使用yield语句和循环语句定义生成器函数

def gen(maxnum):
    for x in range(maxnum):
        yield x

#初始化生成器函数
g=gen(5)

#使用生成器函数时要把生成器函数作为参数调用next()函数

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  #第六次出错，超出了该生成器函数的范围



#使用推导式获得生成器
g=(x for x in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

c=('a',23,43,53,'ni')
g=(x for x in c)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#所以python中没有元组的推导式,使用上述结构得到的只会是生成器


#yield的作用
def dob(a):
    base=10
    i=1
    while i<a:
        h=yield 10*i
        print(i)
        print(h)
        i+=1

g=dob(3)
print(next(g))
print(next(g))

# 使用yield会返回其后面语句的值，并且使得迭代器函数暂停在yield处，直到下一个动作
#如果不使用send的话，迭代语句一般会返回none值





#值的传递，生成器使用send方法将值传递进去
def testSend(mm):
    i=0
    while(i<mm):
        h=yield 10+i
        i+=1
        print(h)


print("测试send")
g=testSend(50)

print(next(g))
# g.send(7)
print(g.send(7))    #使用send相当于使用了输入的值多生成了一次
print(next(g))

#send方法会继续把输入的值代替yield语句继续执行一次迭代函数到又遇到yield为止