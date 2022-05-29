

#类的定义

class Book:
    title='绘卷'
    price=11
    def printPrice(self):
        print(self.getPrice())

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price=price


#类对象的实例化
a=Book()

#通过类对象调用类方法
a.printPrice()
a.setPrice(141)
a.printPrice()


#类使用转换器实例化

class Shelf:
    size=100
    material='木材'
    def __init__(self,size,material):
        print('使用两个参数的转换器')
        self.size=size
        self.material=material


a=Shelf(11,'你好')

