# Author: lisz1012
# Creation date and time: 6/2/24 10:10 PM

import os
path = os.getcwd()  # 获取当前工作目录
lst_files = os.walk(path)  # 列出指定目录下的所有文件和子目录的名称
for dirpath, dirnames, filenames in lst_files:
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))
    print('-------------------')
