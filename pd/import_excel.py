# Author: lisz1012
# Creation date and time: 12/18/22 10:20 PM

import pandas as pd
df = pd.read_excel('京东鞋子评论信息.xlsx', '码数分析', None)
print(type(df))
print(df)

# 仅仅导入姓名这一列数据
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel('02微机原理学员成绩统计.xlsx', 1, usecols=[1, 4])  # '02微机原理及格学员名单'
print(df)
df = pd.read_excel('02微机原理学员成绩统计.xlsx', '02微机原理及格学员名单', usecols=['姓名', '总成绩'])  # '02微机原理及格学员名单'
print(df)