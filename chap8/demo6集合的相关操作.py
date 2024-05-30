# Author: lisz1012
# Creation date and time: 5/29/24 7:38 PM

s = {10, 20, 30, 405, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

s.add(80)
print(s)
s.update({200, 300, 400})   # 以集合的形式添加多个元素
print(s)

s.update([500, 600, 700])   # 以列表的形式添加多个元素
print(s)

s.update((800, 900, 1000))  # 以元组的形式添加多个元素
print(s)

s.update([1, 2], [3, 4])  # 以多个列表的形式添加多个元素
print(s)

s.update({5, 6}, {7, 8})  # 以多个集合的形式添加多个元素
print(s)

s.update((9, 10), (11, 12))  # 以多个元组的形式添加多个元素
print(s)

s.remove(1000)
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 200, 300, 400, 500, 600, 700, 800, 900}

s.discard(100)
print(s)  # 没有 100 也不抛出异常

a = s.pop()  # 随机删除一个元素
print(a)
print(s)

s.clear()
print(s)

# s.remove(100)
# print(s)  # KeyError: 100

s.add([12, 34])  # TypeError: unhashable type: 'list'
