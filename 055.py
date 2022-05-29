
import codecs
#替换文件中的字符串

#把文件path中的字符串old都替换成new
def f_replace(path,old,new):
    if type(path)!=str or type(old)!=str or type(new)!=str:
        print("输入的参数错误")
    else:
        try:
            f=codecs.open(path,'r','utf8')
            sa=list(f)
            f.close()
            n=0
            f=codecs.open(path,'w','utf8')
            for s in sa:
                n+=s.count(old)
                s=s.replace(old,new)
                f.write(s)
            f.close()
            print("替换掉的字符串个数为",n)
        except FileNotFoundError as e:
            print("文件无法正常打开")

#替换字符串
f_replace("dog55.txt","cat","dog")








