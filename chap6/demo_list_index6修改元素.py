# Author: lisz1012
# Creation date and time: 5/27/24 8:34 PM

lst = [10, 20, 30, 40]
# 修改一个值
lst[2] = 100
print(lst)  # [10, 20, 100, 40]
lst[1:3] = [300, 400, 500, 600]  # 切片赋值, 会用新的列表替换原列表的切片 1:3
print(lst)  # [10, 300, 400, 500, 600, 40]
