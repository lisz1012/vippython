# Author: lisz1012
# Creation date and time: 5/28/24 9:25 PM

scores = {'张三': 100, '李四': 98, '王五': 45}
keys = scores.keys()
print(keys)
print(type(keys))  # <class 'dict_keys'>
print(list(keys))  # 转换为列表

values = scores.values()
print(values)
print(type(values))  # <class 'dict_values'>
print(list(values))  # 转换为列表

items = scores.items()
print(items)
print(type(items))  # <class 'dict_items>
print(list(items))  # list of tuples
