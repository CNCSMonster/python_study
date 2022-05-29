class A:
    def __init__(self,pos) -> None:
        self.__pos=pos

    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self,pos):
        self.__pos=pos

    @pos.deleter
    def pos(self):
        del self.__pos

a=A(11)
print(a.pos)
a.pos=55
del(a.pos)

try:
    print(a.pos)
except:
    print("a的pos变量已经删除")


#可以给对象定义新的成员变量
a.dsafd=22
print(a.dsafd)