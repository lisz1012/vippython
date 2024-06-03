# Author: lisz1012
# Creation date and time: 6/2/24 6:05 PM

file = open('a.txt', 'a')  # r: read
# file.write('hello')
lst = ['java', 'python', 'c++']
file.writelines(lst)  # 一次性写入, 但是不会自动换行, 且不会自动添加空格
file.close()
