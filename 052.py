#通过指定文件打开形式，进行重新吸入或者附加写入

#通过w指定重新写入
f=open("by.txt",'w')
n=f.write("ss\nsg")
f.close()

#通过a指定在文件末尾附加写入
f=open("fj.txt",'a+')
if f:
    print("ok to open")
    n=f.write('you')
    f.close()
else:
    print("fail to open the file")


#使用with结构而不是close语句关闭文件对象

#使用了with写法的读出
with open("learnPy.txt",'r') as f:
    for r in f:
        print(r.strip())


#使用了with写法的写入
with open("by.txt",'a') as f:
    f.writelines("You are")






