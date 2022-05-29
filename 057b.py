class A:
    a=1
    t=4
    def __init__(self,a):
        self.a=a
        print("使用A中定义的转换器")

    def show(self):
        print(self.a)

class B:
    b=2
    t=5
    def __init__(self,b):
        self.b=b
        print("使用过B中定义的转换器")

    def show(self):
        print(self.b)


## 测试多继承时继承的父类们中存在同名成员时子类继承哪个
class C(A,B):
    gg=1

a=C(44)
a.show()
print(a.t)

class D(B,A):
    gg=1
a=D(44)
a.show()
print(a.t)

##若子类中存在与父类同名的变量或者方法
class E(A):
    a=5555
    t=6666
    def show(self):
        print("子类定义方法")

a=E(2)
print('t',a.t)
a.show()
#则子类中定义的同名变量和方法会覆盖父类中的变量和方法



