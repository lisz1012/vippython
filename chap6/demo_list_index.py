# Author: lisz1012
# Creation date and time: 5/27/24 8:34 PM

lst = ['hello', 'world', 98]
print(lst.index('world'))  # 1, index 从0开始
lst.append('hello')
print(lst.index('hello'))  # 0, 返回第一个匹配的索引

print(lst.index('hello', 1, 4))  # 3, 从索引1~3的范围内查找


print(lst.index(88))  # ValueError: 88 is not in list

