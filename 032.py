from distutils.errors import LibError
from typing import List


a=[1,2,3,4]
a_db=list()

for b in a:
    a_db.append(b*2)
else:
    print("推导完成a列表的二倍列表")

print(a_db)


#上述代码可以写成如下称为推导式的形式
a_db=[x*2 for x in a]   #该代码可以称作列表的推导式
print(a_db)

#列表推导式还可以像加上条件语句实现选择，
a_db=[x*2 for x in a if x!=3]    #该公式称为列表的条件推导式



