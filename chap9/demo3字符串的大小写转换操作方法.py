# Author: lisz1012
# Creation date and time: 5/30/24 8:25 PM

# 字符串的大写转换
s = 'hello, python'
print(s)
print(id(s))
print(s.upper())
print(s.lower())  # 生成新的字符串, 运行时生成的, 不受驻留机制影响
print(s.swapcase())
print(s.capitalize())
print(s.title())
print(s)
print(id(s))
