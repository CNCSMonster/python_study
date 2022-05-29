#函数的定义

#第一个函数
def doa(a,b):
    c=a+b
    return c

print(doa(1,2))

#不需要参数时可以省略参数
def gethello():
    return "hello"

print(gethello)     #如果输出函数名则输出的是函数名的地址
print(gethello())


#不需要返回值时可以省略返回值

def printHello(name):
    print("Hello",name)

printHello("yjh")


#使用pass定义什么命令都不执行的函数

print("定义并使用没有可执行函数体的函数")

def notdo():
    pass

print(notdo())
notdo()

#若是pass命令在函数中部，则前面部分函数体会执行吗

def testPass():
    print("前面部分")
    pass
    print("后面部分")
    return 1

c=testPass()
print(c)