# Author: lisz1012
# Creation date and time: 12/11/22 3:57 PM

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')  # world会覆盖hello
print('hello\bworld')  # \b是推一个格

print('http:\\\\www.google.com')
print('老师说：\'大家好\'')

# 原字符：让引号中的转义字符不起作用. 注意⚠️字符串的最后一个字符不能是反斜杠 、
print(r'hello\nworld')

# 注意⚠️字符串的最后一个字符不能是反斜杠 \ 实在要输出就用两个反斜杠
print(r'hello\nworld\\')