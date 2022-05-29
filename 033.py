#字典推导式
from random import randint  
#载入模块，使生成随机整数的函数变得可用

keys = ['草莓',9,'橘子',25,'苹果']

d={x:randint(1,100) for x in keys if type(x)==str}

print(d)


#集合推导式

a= [1,2,3,5,626,246,7,3,-35,-66]
setA ={x for x in a if (0<x<=10)}   #与c不同，Python支持双向不等式作为表达式
print(setA)