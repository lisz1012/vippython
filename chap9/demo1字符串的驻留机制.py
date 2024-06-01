# Author: lisz1012
# Creation date and time: 5/29/24 9:03 PM

a = 'Python'
b = "Python"
c = '''Python'''
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))  # 三个字符串的 id 是一样的, 在内存中只有一个对象

s1 = 'abc%'
s2 = 'abc%'
print(s1 is s2)  # True, 不同于交互式
print(s1 == s2)  # True, 这里比较的是值

# 字符串的驻留机制: 编译期间驻留
a = 'abc'
b = 'ab' + 'c'
c = ''.join(['ab', 'c'])  # join()方法比+运算符效率高, 不会+一次就生成一个新的字符串对象
print(a is b)  # True
print(a is c)  # False, 因为 c 是在运行期间生成的

# 交互式中, -5 ~ 256 之间的整数对象会被提前创建好, 供程序使用. 但是在 PyCharm 中做了优化, 会提前创建整数对象
a = -5
b = -5
print(a is b)  # True
a = -1256
b = -1256
print(a is b)  # True

# 强制驻留
import sys
a = sys.intern('hello')
b = sys.intern('hello')
print(a is b)  # True
