# Author: lisz1012
# Creation date and time: 12/28/22 11:00 PM
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
# 制作数据。
data = [
    [45, 46, 100],
    [56, 45, 50],
    [67, 67, 67]
]
index = ['张三', '李四', '王五']
column = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=index, columns=column)
print(df)
# 直接赋值
df['政治'] = [90, 89, 100]
print(df)
# loc属性,在最后一列增加
df.loc[:, '化学'] = [100, 30, 98]
print(df)
# 在指定的索引:1 位置上插入一列
lis = [100, 90, 99]
df.insert(1, '历史', lis)
print(df)
# 按行添加数据
df.loc['赵六'] = [61, 78, 92, 80, 88, 77]
print(df)