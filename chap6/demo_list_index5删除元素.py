# Author: lisz1012
# Creation date and time: 5/27/24 8:34 PM

lst = [10, 20, 30, 40, 50, 60, 30]
print("删除之前:", lst)
lst.remove(30)  # 删除第一个30
print("删除之后:", lst)
lst.pop(2)
print("pop之后:", lst)  # 删除索引为2的元素  [10, 20, 50, 60, 30]
# lst.pop(6)  # IndexError: pop index out of range
lst.pop()  # 删除最后一个元素
print("删除最后一个元素之后:", lst)  # [10, 20, 50, 60]
# lst.remove(100)  # 报错, ValueError: list.remove(x): x not in list

print("-----------------")
new_lst = lst[1:3]  # 切片是原列表的一个拷贝, [1,3)不包括 stop
print("切片:", new_lst)  # [20, 50]
print("原来的 list 不变: ", lst)  # [10, 20, 50, 60]
# 直接将 1-3 的元素挖掉
lst[1:3] = []
print("删除切片后:", lst)  # [10, 60]

# 清除列表中的所有元素
lst.clear()
print("清空列表后:", lst)  # []
# del删除列表对象
del lst
print(lst)  # NameError: name 'lst' is not defined

