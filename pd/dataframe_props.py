# Author: lisz1012
# Creation date and time: 12/18/22 8:20 PM

import pandas as pd
data = [['小太阳', 320.9,  100],
        ['鼠标',   150,    50],
        ['小刀',   1.5,    200]]
columns = ['名称', '单价', '数量']
df = pd.DataFrame(data=data, columns=columns)
print(df)
print("查看所有元素的值\n", df.values) # 打印上面的data
print("查看所有元素的类型\n", df.dtypes)
print("查看所有行的名称\n", df.index)
print("查看所有行的名称\n", list(df.index))
df.index = [1, 2, 3]
print("查看所有行的名称\n", df.index)
print("查看所有行的名称\n", list(df.index))

print("查看所有列索引\n", list(df.columns))
df.columns = ['名称', '单价', 'count']
print("查看所有列索引\n", list(df.columns))
print(df)

# 行列数据转换
df_t = df.T
print(df_t)

pd.set_option('display.unicode.east_asian_width', True)
# df_t = df.T
print(df_t)

# 查看前n跳数据,默认5条
print('查看前N条数据\n', df.head(1))
print('查看后N条数据\n', df.tail(1))

# 查看行、列数
print('行', df.shape[0])
print('列', df.shape[1])

print("查看索引、数据类型、内存信息\n", df.info)
