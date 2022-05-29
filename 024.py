#集合的运算
a={1,2,3}
b={2,3,4}

#集合的乘积
c=a&b 
print(c)
d=a.intersection(b)
print(d)

#集合的和
c=a|b
print(c)
c=a.union(b)
print(c)

#集合的差,这个运算的运算结果与运算次序有关
c=a-b
print(c)
c=b-a
print(c)

#集合的对称差
c=a^b
print(c)

#表现集合间关系的运算
d=c<a
print(d)
d=(a-b)<a
print(d)




