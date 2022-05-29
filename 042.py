#使用split方法进行字符串分割
str='I like apple'
split=str.split(' ')    #把字符串分割得到一个列表
print(split)

#字符串的集合，使用join

s=' '.join(split)
print(s)

# 字符串的替换,使用replace方法

sc='nnttww'
sa=sc.replace('tt','g')
print(sc)
print(sa)