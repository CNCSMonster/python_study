print('%d'%3)
a=3
print('%d'%a)
print("3")
print("%d比%d小"%(2,3))
print("%d乘以%d等于%d"%(2,3,(2*3)))
a=255
print('%d'%a)
print('%x'%a)
print("%X"%a)
print('%.3f'%a)
print("\n%f"%a)
a='nihao'
print('%s\tyjh'%a)
#左对齐与右对齐
print('%-5d'%334)#前面加负号左对齐
print('%5d'%334)
print('%04d'%334)

#
#'pgsql2shp -f D://result.shp -u postgres -P 102301 -h 127.0.0.1 -d test "SELECT * FROM chenyi WHERE name_0 ='France' "'

path='pgsql2shp -f D://result.shp -u postgres -P 102301 -h 127.0.0.1 -d test "SELECT * FROM chenyi WHERE name_0 =\'France\' \"'
print(path)

