class A:
    def __init__(self,t,v):
        self.title=t
        self.__v=v ##使用两个下划线来隐藏v变量，使得其不能被直接访问


a=A(22,33)
print(a.title)
a.title=33
print(a.title)
del a.title
try:
    print(a.title)
except:
    print('a中title成员不存在')
# print(a.__v)  #非法语句，使用了__隐藏的变量无法轻易访问



class B:
    __name='你好'
    def __init__(self,name,v) -> None:
        self.__name=name
        self.__v=v

    def setV(self,v):
        self.__v=v
        print('使用自定义的设定方式')

    def getV(self):
        print('使用自定义的访问方式')
        return self.__v
    
    def delV(self):
        print("使用自定义的删除方式")
        del self.__v

    v=property(fget=getV,fset=setV,fdel=delV,doc='B类的值')


##使用property函数定义了属性之后，
# 原本使用__隐藏的变量又可以访问设定删除了，
# 不过是使用我们定义的函数来进行
b=B('nb',55)
b.v=44
print(b.v)
del(b.v)