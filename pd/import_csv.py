# Author: lisz1012
# Creation date and time: 12/18/22 10:34 PM

import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('京东鞋子评论数据.csv', sep=',', encoding='gbk')
print(df)
print(df.head())