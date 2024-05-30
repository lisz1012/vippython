# Author: lisz1012
# Creation date and time: 5/29/24 8:14 PM

# 交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)

# 并集
print(s1.union(s2))
print(s1 | s2)

# 差集
print(s1.difference(s2))
print(s1 - s2)

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 原来的s1, s2不变
print(s1)
print(s2)
