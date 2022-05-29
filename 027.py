#python 的if-elif-else语句
i=8
if i>10:
    print("是一个大于10的数")
elif i>8:
    print("i<=10&&i>8")
elif i>4:
    print("i>4&&i<=8")
else:
    print("i小于4")


#if语句的嵌套

if i>4:
    if i>10:
        print("是一个大于10的数")
    elif i>8:
        print("i<=10&&i>8")
    else:
        print("i>4&&i<=8")
else:
    print("i小于4")


