# Author: lisz1012
# Creation date and time: 6/2/24 6:05 PM

file = open('a.txt', 'r')  # r: read
# print(file.read())  # 读取文件的全部内容
# print(file.read(2))  # 读取文件的前2个字符
# print(file.readline())  # 读取文件的一行
# print(file.readline())
print(file.readlines())
file.close()
