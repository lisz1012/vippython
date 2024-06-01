# Author: lisz1012
# Creation date and time: 5/31/24 8:22 PM

name = '张三'
age = 20
print('我叫%s, 今年%d岁了' % (name, age))

print('我叫{0}, 今年{1}岁了, 我真的叫{0}'.format(name, age))
print(f'我叫{name}, 今年{age}岁了, 我真的叫{name}')

print('--' * 20)
print('%10d' % 99)   # 右对齐, 撑满10个字符
print('%-10d' % 99)  # 左对齐, 撑满10个字符
print('%010d' % 99)  # 右对齐, 撑满10个字符, 不足的用0填充
print('%.3f' % 3.1415926)  # 保留3位小数, 4舍5入
print('%10.3f' % 3.1415926)  # 右对齐, 保留3位小数, 4舍5入, 且撑满10个字符
print('hellohello')

print('--' * 20)
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # 一共是 3 位数, 4 舍 5 入
print('{0:.3f}'.format(3.1415926))  # 保留 3 位小数, 4 舍 5 入
print('{:.3f}'.format(3.1415926))  # 保留 3 位小数, 4 舍 5 入
print('{:10.3f}'.format(3.1415926))  # 右对齐, 保留 3 位小数, 4 舍 5 入, 撑满 10 个字符
