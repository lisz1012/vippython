# Author: lisz1012
# Creation date and time: 6/2/24 9:25 PM

import os
print(os.getcwd())  # 获取当前工作目录
print(os.listdir())  # 获取当前目录下的所有文件和文件夹
lst = os.listdir('subdir')
print(lst)
print(os.path.exists('subdir'))  # 判断subdir是否存在
print(os.path.abspath('subdir'))  # 获取subdir的绝对路径
if not os.path.exists('subdir2'):
    os.mkdir('subdir2')  # 创建subdir2文件夹
print(os.path.abspath('subdir2'))

if not os.path.exists('subdir3'):
    os.makedirs('subdir3/subdir4')  # 创建subdir3文件夹, 创建多级目录

if os.path.exists('subdir2'):
    os.rmdir('subdir2')  # 删除subdir2文件夹

if os.path.exists('subdir3'):
    os.removedirs('subdir3/subdir4')  # 删除subdir3文件夹, 删除多级目录

os.chdir('/Users/shuzheng/Documents')
print(os.getcwd())  # 获取当前工作目录
print(os.listdir())  # 获取当前目录下的所有文件和文件夹
os.chdir('/Users/shuzheng/PycharmProjects/vippython/chap15')

print('---------os.path---------')
print(os.path.abspath('demo13os模块的常用函数.py'))  # 获取subdir的绝对路径
print(os.path.exists('demo13os模块的常用函数.py'), os.path.exists('demo18.py'))  # 判断文件是否存在
# join()函数用于路径拼接
print(os.path.join(os.getcwd(), 'subdir', 'a.txt'))
print(os.path.split(os.path.abspath('demo13os模块的常用函数.py')))  # 分割路径, 结果是元组
print(os.path.split('chap15/demo13os模块的常用函数.py'))  # 分割文件名, 结果是元组
print(os.path.splitext('demo13os模块的常用函数.py'))  # 分割文件名和后缀 .py, 结果是元组

print('---------os.path---------')
print(os.path.basename(os.path.abspath('demo13os模块的常用函数.py')))  # 获取文件名
print(os.path.dirname(os.path.abspath('demo13os模块的常用函数.py')))  # 获取文件路径
print(os.path.isfile('demo13os模块的常用函数.py'))  # 判断是否是文件
print(os.path.isdir('demo13os模块的常用函数.py'))  # 判断是否是文件夹
print(os.path.getsize('demo13os模块的常用函数.py'))  # 获取文件大小
print(os.path.getatime('demo13os模块的常用函数.py'))  # 获取文件的最后访问时间
print(os.path.getmtime('demo13os模块的常用函数.py'))  # 获取文件的最后修改时间
print(os.path.isdir('/Users/shuzheng/PycharmProjects/vippython/chap15'))  # 判断是否是文件夹
