class Book:
    title='绘卷'
    price=11

    def printPrice(self):
        print(self.getPrice())

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price=price

class Square:
    chang=22
    kuang=13
    def printChang(self):
        print('chang:',self.chang)

#类的继承
class ColorBook(Book,Square):
    color='绿色'

#子类的实例化，可以使用父类的转换器
#如果父类和子类都没有定义转换器，则使用默认的创建方法，类名()
cb=ColorBook()
cb.printPrice()
cb.printChang()


