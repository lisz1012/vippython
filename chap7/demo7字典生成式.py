# Author: lisz1012
# Creation date and time: 5/28/24 9:45 PM

items = ['Fruits', 'Books', 'Others']
prices = [100, 200, 300]
d = {item: price for item, price in zip(items, prices)}
print(d)

items = ['Fruits', 'Books', 'Others']
prices = [100, 200]
d = {item: price for item, price in zip(items, prices)}
print(d)  # {'Fruits': 100, 'Books': 200} # 由于zip函数会按照最短的序列进行组合, 所以'Others'这个元素被忽略了

items = ['Fruits', 'Books']
prices = [100, 200, 300]
d = {item: price for item, price in zip(items, prices)}
print(d)  # {'Fruits': 100, 'Books': 200} # 由于zip函数会按照最短的序列进行组合, 所以'300'这个元素被忽略了
