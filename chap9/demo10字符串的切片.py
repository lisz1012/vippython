# Author: lisz1012
# Creation date and time: 5/31/24 8:05 PM

s = 'hello,Python'
s1 = s[:5]  # 没指定开始位置, 默认从0开始
s2 = s[6:]  # 没指定结束位置, 默认到最后一个字符
s3 = '!'
new_str = s1 + s3 + s2

print(s1)
print(s2)
print(new_str)
print('--' * 20)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))  # 字符串是不可变对象, 每次操作都会生成新的字符串
print('--' * 20)
print(s[1:5:1])  # ello
print(s[::2])  # 步长是 2, 隔一个取一个
print(s[::-1])  # 步长是 -1, 逆序输出, 默认从最后一个字符开始, 因为步长是负数
print(s[-6::1])  # Python
