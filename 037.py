from ast import arg


def doa(a,b):
    return a-b

print(doa(10,20))



#使用了关键字的参数指定
print(doa(a=10,b=20))
print(doa(b=10,a=20))

#还可以使用位置和关键字参数混合指定
def doc(a,b,c):
    print('a=',a,'b=',b,'c=',c)

#如下，首字母采用了位置指定，后面两个字母采用了关键字参数指定
doc(1,c=2,b=3)

#参数的全局调用


#把参数当做元组接收
print("把参数当做元组接收")
def avg(*args):
    print(args)
    for x in args:
        print(x)

avg(12,3,'a')

#把参数当做字典接收
print("把参数当做字典接收")
def mydict(**args):
    return args

dic=mydict(s=20,b=33,c=55)
print(dic)









