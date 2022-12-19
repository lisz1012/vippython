# Author: lisz1012
# Creation date and time: 12/17/22 7:59 PM

a, b = 1, 2
print(a == 1 and b == 2)
print(a == 1 and b < 2)
print(a != 1 and b == 2)
print(a != 1 and b != 2)
print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)
print(a == 1)
print(not(a == 1))
f = True
print(not f)

# in and not in
s = 'hello world'
print('w' in s)
print('k' in s)
print('hello' in s)
print('k' not in s)