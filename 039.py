#使用无名函数

#使用lambda关键字来定义和使用无名函数

from audioop import mul

fa=lambda s,b:s+b
print(fa(1,2))

lo=lambda s:s.lower()

print(lo("HELLO"))

#与直接使用函数的效果一样，
def toL(s):
    return s.lower()

print(toL("HELLO"))


#回调函数
def multiply(a,b):
    return a*b

def minus(a,b):
    return a-b

#在func中以callback作为函数参数，
def func(a,b,callback):
    return callback(a,b)

#
print(func(1,2,multiply))

#使用minus作为回调函数调用func函数
print(func(1,2,minus))


