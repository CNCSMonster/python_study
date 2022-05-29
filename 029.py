# 利用range

#range(上限)，默认为0，增量默认为1，注意这里的上限是不可以达到的
for a in range(7):
    print(a)

# range(开始，上限（不可到达），增量)
for a in range(2,42,5):
    print(a)

#利用range创建列表
a=list(range(1,11,2))
print(a)
