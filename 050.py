import re
from tokenize import String


#判断输入的密码是否符合要求，
#要求只能使用小写英文和数字和下划线，且首字母必须是a
#密码字符数量5个以上，10个以下

while True:
    s=input('密码>')
    if s=='':
        break
    reobj=re.compile("^a[0-9a-z]{4,9}$")
    mobj=reobj.match(s)
    if mobj:        #如果匹配成功
        print("密码格式正确")
    else:
        print('密码格式不正确')



#判断是否是中文
def ifCnC(ch):  #判断是否是中文字符
    #python采用unicode编码
    if '\u4e00' <= ch <= '\u9fff':
        return True
    else:
        return False


def ifChinese(s):
    ca=list(s)
    for x in ca:
        if not ifCnC(x):
            return False
    return True


while True:
    s=input('中文>')
    if s=='':
        break
    ifc=ifChinese(s)
    if ifc:        #如果匹配成功
        print("输入为中文字符串")
    else:
        print('输入不是中文字符串')





s='nihao'
print(type(s))