# Author: lisz1012
# Creation date and time: 5/30/24 8:32 PM

s = 'hello,python'
print(id(s))
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.ljust(10, '*'))  # 如果指定的宽度小于字符串的宽度, 则返回原字符串
print(id(s.ljust(10, '#')))  # 宽度小于字符串的宽度, 返回原字符串
print(s.rjust(20, '*'))
print(s.rjust(20))  # 默认填充空格
print(s.zfill(20))
print(s.zfill(10))  # 如果指定的宽度小于字符串的宽度, 则返回原字符串
print('-8910'.zfill(8))  # -0008910
