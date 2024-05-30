# Author: lisz1012
# Creation date and time: 5/29/24 6:12 PM

t = (10, [20, 30], 9)
print(t)
print(id(t))
print((type(t)))
print(t[0])
print(t[1])
print(t[1][0])
print(t[1][1])
print(t[2])

print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))

t[1].append(100)
print(t[1])
print(id(t[1]))  # 地址不变
t[1] = 100  # TypeError: 'tuple' object does not support item assignment
