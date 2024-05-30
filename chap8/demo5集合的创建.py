# Author: lisz1012
# Creation date and time: 5/29/24 6:25 PM

s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不允许重复
print(s)

s = set(range(6))  # 通过 range() 函数创建集合
print(s)  # {0, 1, 2, 3, 4, 5}
print(type(s))  # <class 'set'>

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 通过列表创建集合
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(s))  # <class 'set'>

s = set((1, 2, 3, 4, 5, 6, 7, 8, 9))  # 通过元组创建集合
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(s))  # <class 'set'>

s = set('Python')  # 通过字符串创建集合
print(s)  # {'h', 't', 'P', 'y', 'n', 'o'}
print(type(s))  # <class 'set'>

s = set({'name': 'Python', 'age': 30})  # 通过字典创建集合
print(s)  # {'name', 'age'}
print(type(s))  # <class 'set'>

s = set({124, 3, 4, 4, 5}) # 通过集合创建集合
print(s)  # {4, 3, 124, 5}
print(type(s))  # <class 'set'>

s = {}  # 创建空字典
print(s)  # {}
print(type(s))  # <class 'dict'>

s = set()
print(s)  # set()
print(type(s))  # <class 'set'>
