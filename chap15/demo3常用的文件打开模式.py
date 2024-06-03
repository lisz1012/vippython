# Author: lisz1012
# Creation date and time: 6/2/24 5:48 PM

file = open('b.txt', 'w')  # w: write 其路径就是当前文件夹下, 会抹掉已有的内容
file.write('Python')
file.write('Java')  # PythonJava
file.close()
