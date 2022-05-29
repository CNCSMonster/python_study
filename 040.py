#本地变量与全局变量演示

a=1     #全局变量
def doa():
    b=2     #函数doa的全局变量，作用范围在doa内
    def dob():
        c=3 #嵌套函数dob的局部变量，作用范围在dob之内
        print(a,b,c)
    dob()

doa()

#使用global和nonlocal声明非本地变量

a=2
print(a)
def doC():
    # print(a)
    # a在该函数中若是有赋值行为则被认为是在函数中形成了一个本地同名变量a,
    # 而上述语句意思为打印全局变量a,python中a不能够在一个模块中同时为全局变量
    # 和本地变量，所以上述语句与下述语句矛盾
    a=3         #在doC中没有特别声明a为全局变量，则默认为本地变量，对其操作实际上没有修改到全局a

doC()
print(a)

#使用global声明全局变量
def doD():
    global a
    a=3

doD()
print(a)

#使用nonlocal声明本地变量

def doE():
    b=1
    c=1
    def func():
        nonlocal b  #晟敏b为非本地变量，则b不被视为嵌套函数func中的本地变量，而是被视为外部函数模块的本地变量
        b=2
        c=3
        print(b,c)
    func()
    print("经过内部嵌套函数修改后")
    print(b,c)

doE()