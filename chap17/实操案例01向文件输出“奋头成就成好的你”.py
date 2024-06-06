# Author: lisz1012
# Creation date and time: 6/4/24 10:51 PM

# 使用 print() 函数向文件输出内容
with open('test.txt', 'w') as f:
    print('奋斗成就更好的你', file=f)

# 使用文件读写操作
with open('test.txt', 'a') as f:
    f.write('奋斗成就更好的你\n')
