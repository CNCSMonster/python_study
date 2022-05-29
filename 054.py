##例外处理的结构


#try:
#   可能出现例外的语句
#except 例外类名 as 变量名：
#   发生了例外时的处理方法，处理完跳出try-except-else结构
#else:
#   没有发生例外时执行的语句
#例外处理外的语句

#让例外情况发生
try:
    raise Exception("例外","错误")
except Exception as e:
    a,b=e.args
    print("a=",a,"b=",b)

#处理找不到文件时的例外情况

try:
    f=open("cuo.txt",'r')
    f.close()
except FileNotFoundError:
    print("找不到文件")
except Exception as e:
    print(e.args)
else:
    print("文件正常读取")
