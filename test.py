f=open("by.txt",'w')
n=f.write("ss\nsg")
f.close()

f=open("fj.txt",'a+')
if f:
    print("ok to open")
    n=f.write('you')
    f.close()
else:
    print("fail to open the file")