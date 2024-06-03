# Author: lisz1012
# Creation date and time: 6/2/24 10:07 PM

import os

path = os.getcwd()  # 获取当前工作目录
lst = os.listdir(path)  # 列出指定目录下的所有文件和子目录的名称
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
