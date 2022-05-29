#文件的开闭




f=open("learnPy.txt",'r')   #使用只读方式打开文件对象流
f.close()   #关闭文件对象流


#读取文件

#最常见的读取方式，逐行读取
f=open("learnPy.txt",'r')   #使用只读方式打开文件对象流
for x in f:
    # print(x)
    print(x.strip())
f.close()

#仅仅读取一行
print("仅仅读取一行")
f=open("learnPy.txt",'r')   #使用只读方式打开文件对象
s=f.readline()
print(s)
f.close()

#只读取指定的字节数
print("只读取指定的字节数")
f=open("learnPy.txt",'r')   #使用只读方式打开文件对象
s=f.read(4)
print(s)
f.close()

#读取全部
print("读取全部")
f=open("learnPy.txt",'r')   #使用只读方式打开文件流对象
sl=f.read()
print(sl)
f.close()

#读取为字符串列表
print("使用read不传参读取出字符串列表")
f=open("learnPy.txt",'r')   #使用只读方式打开文件对象
sl=f.readlines()
print(sl)
f.close()

#使用list由文件对象生成字符串列表
print("使用list直接由文件对象生成字符串列表")
f=open("learnPy.txt",'r')   #使用只读方式打开文件对象流
sl=list(f)
print(sl)
f.close()












