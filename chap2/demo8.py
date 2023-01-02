# Author: lisz1012
# Creation date and time: 12/17/22 4:48 PM

name = 'zhangsan'
age = 18
print(name, type(name))
print(age, type(age))
print('我叫' + name + '今年' + str(age) + '岁') # 加上str()，否则报错
print(int('18')+1)
print(float('3.14') + 1)

a = 10
b = 198.5
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(a)))

s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'

print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1))
print(int(f1))
#print(int(s2)) '76.77'不会被取整，而是直接报错。
print(int(ff))
#print(int(s3))

s1 = '128.98'
f1 = 98
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(ff), type(s3))
print(float(s1), type(float(s1)))
print(float(f1), type(float(f1)))
print(float(ff), type(float(ff)))
print(float(s3), type(float(s3)))