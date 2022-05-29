from asyncio import WindowsSelectorEventLoopPolicy
from ctypes import Union
from random import randint

user_numbers=list()
lucky_numbers=list()
print("请输入1-10之间的5个数字")

#选择参加测试的数字
while 0<=len(user_numbers)<5:
    input_numbers=input("< ")
    try:
        a=int(input_numbers)
    except:
        print('输入错误,请重新输入')
        continue
    if 0>a or a>10:
        print(a,"不是1-10之间的数,请重新输入",sep=' ')
    elif a in user_numbers:
        print(a,"已经输入过了,请重新输入",sep=' ')
    else:
        user_numbers.append(a)


print("你选择的数字是：",user_numbers)

#随机获得1-10之间的幸运数字
print("现在开始抽选:")

for a in range(1,6):
    b=randint(1,10)
while b in lucky_numbers:
    b=randint(1,10)
    lucky_numbers.append(b)

print(lucky_numbers)

print("中选数字是：")

# 传统方法，循环取同

# python利用包装类型方法，化为集合取交

# userset=set(user_numbers)

# luckset=set(lucky_numbers)

# winset=userset.intersection(luckset)

# python的推导式方法

winset={x for x in user_numbers if x in lucky_numbers}

print(winset)