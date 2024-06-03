# Author: lisz1012
# Creation date and time: 6/2/24 6:40 PM

# with 语句, 无需手动关闭文件
# print(type(open('a.txt', 'r')))
with open('a.txt', 'r') as file:
    print(file.read())
