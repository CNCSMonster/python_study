import sys
from tokenize import Double

#输入的头两个数为加数

fadd=lambda a,b:a+b

if len(sys.argv)>=3:
    try:
        a=float(sys.argv[1])
        b=float(sys.argv[2])
        print(fadd(a,b))
    except:
        print('输入的参数错误')