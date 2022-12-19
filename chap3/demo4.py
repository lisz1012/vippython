# Author: lisz1012
# Creation date and time: 12/17/22 7:16 PM

a = 3 + 5
print(a)
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

a = 20
a += 30
print(a)
a -= 10
print(a)
a *= 2
print(a)
a //= 2
print(a)
print(a, type(a))
a /= 2
print(a, type(a))
a %= 3
print(a, type(a))

a, b, c = 2, 3, 4
print(a, b, c)

# 交换两个变量的值
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)