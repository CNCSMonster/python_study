# break
a=0
b=5
while a<5:
    if  (b-a)<=0:
        break
    print(b-a)
    a+=1
#上：a循环打印、增大直到不小于b,每次

#continue

a=[1,2,4,'你',12.4,23]
for key in a:
    if type(key)!=int:
        print(key)
        if type(key)==float:
            print("是小数")
        elif type(key)==str:
            print("是字符串")
        print("不是整数")
        continue
    print(key)