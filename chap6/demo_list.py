# Author: lisz1012
# Creation date and time: 5/27/24 8:17 PM

lst = ['hello', 'world', 98]
lst2 = list(['hello', 'world', 98])

print(id(lst))
print(type(lst))
print(lst)

for i in lst:
    print(i)

print(id(lst2))
print(type(lst2))
print(lst2)

for i in range(lst2.__len__()):
    print(lst2[i])

lst2.append('python')
print(lst2[-3])  # 倒数第三个元素
