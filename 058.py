class A:
    a=1
    def __init__(self,a):
        self.a=a
        print("使用A中定义的转换器")

    def showA(self):
        print(self.a)

class B(A):
    b=2
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("使用过B中重写的转换器")

    def showA(self):
        super().showA()
        print(self.b)

a=A(33)
a.showA()

b=B(2,3)
b.showA()