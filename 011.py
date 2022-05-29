# 逻辑运算符:and(与)，or(或)，not(非)
a=1<3
b=2>3
print("a的值是",a)
print('b的值是',b)
print(a and b)
print(a or b)
print(not a)
print(not b)
print(a and (not b))
print((not a) or b)

# 三目运算符
point=98
a='优秀'if point > 90 else '不及格'
print('小生的成绩',a,sep='')


