# Author: lisz1012
# Creation date and time: 6/2/24 5:58 PM

src_file = open('logo.png', 'rb')
dst_file = open('logo2.png', 'wb')
dst_file.write(src_file.read())  # 拷贝文件: 读取源文件的内全部容, 写入目标文件
src_file.close()
dst_file.close()
