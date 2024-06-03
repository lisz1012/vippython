# Author: lisz1012
# Creation date and time: 6/2/24 6:05 PM

file = open('a.txt', 'r')  # r: read
file.seek(3)  # 移动指针到第3个字符
print(file.read())  # 读取文件的全部内容
print(file.tell())  # 获取指针的位置
file.close()
