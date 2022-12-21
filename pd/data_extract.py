# Author: lisz1012
# Creation date and time: 12/18/22 11:22 PM

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
# 制作数据
data = [
    [45, 46, 100],
    [56, 45, 50],
    [67, 67, 67]
]
index = ['张三', '李四', '王五']
column = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=index, columns=column)
print(df)

# 提取单行数据
print(df.loc['张三'])
print(df.iloc[0])
# 提取多行数据
print("提取多行数据\n", df.loc[['李四', '王五']])
print(df.iloc[[0, 2]])
print("提取连续的多行数据（从谁到谁）", df.loc['张三':'王五'])  # 包含王五
print(df.iloc[0:2])  # 不包含2号的王五
print(df.iloc[1::])  # 从1开始（包括1），直到最后（包含），步长是1
print(df.iloc[::2])  # 从0开始（包括0），直到最后（包含），步长是2

# 提取列数据。
print(df[['数学', '英语']])  #  最简单
print(df.loc[:, ['语文', '英语']])  # 提取所有行的语文和英语. , 左边的是行右边的是列
print(df.iloc[:, [0, 2]])
print(df.loc[:, '数学':])  # 两个:也行
print(df.iloc[:, 1:])  # 两个:也行
