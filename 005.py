





print('nihao{}'.format('yjh'))
print('{1}位置是{0}'.format(3,4))
a='中国'
b='发展中国家'
print("{}是一个{}".format(a,b))
print(f'{a}是一个{b}')
print(f"{a}是一个{b}")

# 使用format输出的方法中指定格式使用{:格式符号}
a=232
print("a等于{:d}".format(a))

# 每三位数进行一次区分
a=2324243
print("{:,}".format(a))

# 位数和显示位置
a=23
print('{:<4}'.format(a))    #显示左对齐的四位数
print('{:>4}'.format(a))    #右对齐
print('{:^4}'.format(a))    #居中显示四位数

print('use f\'\' form')
print(f'{a:<4}')
print(f'{a:>4}')    #右对齐
print(f'{a:^4}')    #居中显示四位数

# 可以使用0、,格式
print(f'{a:0<4}')
print(f'{a:|>4}')    #右对齐
print(f'{a:a^4}')    #居中显示四位数

# 由上述结果可知，在{:}形式中后面使用的<,>,^文本位置符号
# 前面如果填上什么字符，空位就会补上什么字符







