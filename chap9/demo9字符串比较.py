# Author: lisz1012
# Creation date and time: 5/31/24 7:57 PM

print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(chr(97), chr(98))
print((ord('李')))
print(chr(26446))

# == 和 is 的区别: == 比的是 value, 而 is 比的是地址, id
a = b = 'Python'
c = 'Python'
print(a == b)
print(a == c)
print(a is b)
print(a is c)
d = 'Pyt' + 'hon'
print(a == d)
print(a is d)  # True, 因为 d 是在编译期间就生成的
