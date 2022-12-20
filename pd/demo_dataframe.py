# Author: lisz1012
# Creation date and time: 12/18/22 5:17 PM

import pandas as pd
# 列表方式
data = [['小太阳', 320.9,  100],
        ['鼠标',   150,    50],
        ['小刀',   1.5,    200]]
columns = ['名称', '单价', '数量']
df = pd.DataFrame(data=data, columns=columns)
print(df)
print(type(df))

# 字典方式
data = {
    '名称': ['小太阳', '鼠标', '小刀'],
    '单价': [328.9, 150, 1.5],
    '数量': [100, 50, 200]
}
df = pd.DataFrame(data=data)
print(df)

# data = {
#     '名称': ['小太阳', '鼠标', '小刀', '铅笔'], # 列表长度一致
#     '单价': [328.9, 150, 1.5],
#     '数量': [100, 50, 200]
# }
# df = pd.DataFrame(data=data)
# print(df)

data = {
    '名称': ['小太阳', '鼠标', '小刀'],
    '单价': [328.9, 150, 1.5],
    '数量': [100, 50, 200],
    '公司名称': '东门超市'
}
df = pd.DataFrame(data=data)
print(df)