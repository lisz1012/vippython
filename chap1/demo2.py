# Author: lisz1012
# Creation date and time: 12/11/22 3:57 PM

print('hello\nworld')
print('hello\tworld')  # \t 占了 3 个字符. 第一个 o 占了一个
print('helloooo\tworld')  # 头 4 个 o 占满了 4 个字符, \t 占了 4 个字符,占满就重新开制表位,否则不重新开
print('hello\rworld')  # world会覆盖hello
print('hello\bworld')  # \b是退一个格
print('hello\b')  # o被删除

print('http:\\\\www.google.com')
print('老师说：\'大家好\'')

# 原字符：让引号中的转义字符不起作用. 注意⚠️字符串的最后一个字符不能是反斜杠 、
print(r'hello\nworld')

# 注意⚠️字符串的最后一个字符不能是反斜杠 \ 实在要输出就用两个反斜杠
print(r'hello\nworld\\')