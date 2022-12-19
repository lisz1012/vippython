# Author: lisz1012
# Creation date and time: 12/17/22 7:33 PM

a, b = 1, 2
print('a > b ? ', a > b)
print('a < b ? ', a < b)
print('a >= b ? ', a >= b)
print('a <= b ? ', a <= b)
print("a == b ? ", a == b) # 比较的是value，值
print("a != b ?", a != b)
# 比较对象的标识用is
a = 11256
b = 11256
print(a == b)
print(a is b) # 内存里有11256这个值了，就不再创建对象了

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]

print(list1 == list2)
print(list1 is list2)
print(id(list1), id(list2))
print(a is not b)
print(list1 is not list2)