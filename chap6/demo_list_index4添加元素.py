# Author: lisz1012
# Creation date and time: 5/27/24 8:34 PM

lst = [10, 20, 30]
print("添加之前:", lst)
print("添加之前list的id:", id(lst))
lst.append(40)
print("添加之后:", lst)
print("添加之后list的id:", id(lst))  # id不变, 说明是在原列表上进行操作

lst2 = ['hello', 'world']
lst.append(lst2)
print("添加lst2之后:", lst)
lst.pop()
print("删除之后:", lst)
lst.extend(lst2)
print("用extends添加lst2之后:", lst)

lst.insert(1, 90)
print("在索引1处插入90:", lst)

lst3 = [True, False, 'hello']
lst[1:] = lst3  # 切片赋值, 会用新的列表替换原列表的切片 1:
print("切片赋值:", lst)
lst = [10, 20, 30, 40, 50]
lst[::2] = lst3  # 步长为2的切片赋值, 其实是将lst3的元素替换掉lst的元素
print("步长为2的切片赋值:", lst)  # [True, 20, False, 40, 'hello']
