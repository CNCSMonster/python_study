#ͨ��ָ���ļ�����ʽ����������������߸���д��

#ͨ��wָ������д��
f=open("by.txt",'w')
n=f.write("ss\nsg")
f.close()

#ͨ��aָ�����ļ�ĩβ����д��
f=open("fj.txt",'a+')
if f:
    print("ok to open")
    n=f.write('you')
    f.close()
else:
    print("fail to open the file")


#ʹ��with�ṹ������close���ر��ļ�����

#ʹ����withд���Ķ���
with open("learnPy.txt",'r') as f:
    for r in f:
        print(r.strip())


#ʹ����withд����д��
with open("by.txt",'a') as f:
    f.writelines("You are")






