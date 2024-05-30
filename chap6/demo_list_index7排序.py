# Author: lisz1012
# Creation date and time: 5/27/24 8:34 PM

lst = [20, 40, 10, 98, 54]
print("排序之前:", lst)
print(id(lst))
lst.sort()
print("排序之后:", lst)
print(id(lst))
lst = [20, 40, 10, 98, 54]
lst.sort(reverse=True)
print("逆序排序之后:", lst)
lst[1:4].sort()
print("排序之后:", lst)

print("-----------------")

lst = [20, 40, 10, 98, 54]
print("使用内置函数排序之前:", lst, id(lst))
new_list = sorted(lst)
print("使用内置函数排序之后:", new_list, id(new_list))
