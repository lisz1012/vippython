# Author: lisz1012
# Creation date and time: 12/18/22 4:56 PM

import pandas as pd
data = ['C罗', '梅西', '姆巴佩']

s = pd.Series(data=data)
print(type(s))
print(s)

s = pd.Series(data=data, index=[1, 2, 3])
print(s)

data = [90, 98, 87]
index = ['张三', '李四', '王五']
s = pd.Series(data=data, index=index)
print(s)
print(s['张三'])  # 标签索引
print(s[['张三', '王五']])

data = ['C罗', '梅西', '姆巴佩']
s = pd.Series(data=data)
print(s[0])      # 位置索引
print(s[1:5:1])

data = [90, 98, 87]
index = ['张三', '李四', '王五']
s = pd.Series(data=data, index=index)
print(s['张三':'王五'])   # 头尾都包括
print(s['张三':'王五1'])  # 并不会报错
print(list(s.index))
print(s.values)
print(type(s.values))   # s.values 并不是列表