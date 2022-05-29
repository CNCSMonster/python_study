import codecs
from encodings import utf_8

#指定编码格式打开文件写入
f=codecs.open('zdbm.txt','w','utf8')
f.write("你好")
f.close()

with codecs.open('zdbm.txt','a','utf8') as f:
    f.write("\n飞行员")



#指定编码格式打开文件读出
f=codecs.open('zdbm.txt','r','utf8')
for s in f:
    print(s.strip())
f.close()

with codecs.open('zdbm.txt','r','utf8') as f:
    sl=f.readlines()
    print(sl)



