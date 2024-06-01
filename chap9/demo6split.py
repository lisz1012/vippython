# Author: lisz1012
# Creation date and time: 5/31/24 6:34 PM

s = 'hello world python'
lst = s.split(' ')
print(lst)
lst2 = s.split(' ', 1)  # 以空格分割, 分割一次, 从左边开始切割, 切一刀
print(lst2)
lst3 = s.split()  # 默认以空格分割
print(lst3)

s1 = 'hello|world|python'
print(s1.split())  # 默认以空格分割, 没有空格, 故不分割. 但是输出结果是原字符串的列表
print(s1.split('|'))  # 以|分割

print(s.rsplit())  # 默认以空格分割
print(s1.rsplit('|'))  # 以空格分割
print(s1.rsplit('|', 1))  # 以|分割, 从右边开始切割, 切一刀
