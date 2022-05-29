
#使用strip去掉无效空格
s1="   ni    hao dsd    "
print(s1.strip())  #默认会去掉前后空格

s1=".... dsd sd adfa....   "
print(s1.strip())
print(s1.strip('.'))    #可以指定前后要去掉的符号
print(s1.strip(". "))   #可以指定多个要去掉的符号，用字符串形式输入


#大小写和首字母转换
s='water'
s=s.upper()
print(s)
s=s.lower()
print(s)
s=s.title()
print(s)


#转换为字符串
#可以使用str把各种类型转化为字符串
a=('s',"nihao",'d',[1,2,3],True,{3,'g'})
print(str(a))
for x in a:
    print(str(x))



#用len获得字符串长度
print(len(str(111)))

#使用索引任意截取字符串
s="0123456789abc"
print(s[:])
print(s[4:9])
print(s[-5:-3])
print(s[:4])
print(s[-9:])




#使用循环语句从字符串中逐一取出文字，在这里其实是把字符串当做迭代器对象处理

s='ni hao'
for x in s:
    print(x)

