#使用find方法检索字符串中特定字符串的位置
a='I like you.you like apple'
n=a.find('like')
print(n)    #返回的是匹配的总串中左下标

#可以限定检索范围
n=a.find('like',5,20)
print(n)
#输入的前后两个下标分别是：开始下标，结束下标+1

#如果没有找到，返回-1值
n=a.find('il')
print(n)
n=a.find('l',2,2)
print(n)

#查看特定字符串是否被包含,in 和 not in

print('you' in a)
print('ggg' in a)

#调查字符串的个数
s="我为人人人人为我"
print(s.count("人人"),s.count("ni"))