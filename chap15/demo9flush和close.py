# Author: lisz1012
# Creation date and time: 6/2/24 6:05 PM

file = open('d.txt', 'w')
file.write('hello')
file.close()
file.write('world')  # 报错, 因为文件已经关闭, 文件中只有 hello, 所以 close 之后就不能再操作了, 但是 flush 之后还可以操作
file.flush()
file.close()
