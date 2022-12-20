# Author: lisz1012
# Creation date and time: 12/18/22 11:04 PM

import pandas as pd
url = 'http://www.espn.com/nba/salaries'
df = pd.DataFrame()
df = df.append(pd.read_html(url, header=0))  # 第一行是标题行， 只能读出带有table标签的
print(df)
print(df.max())

# 保存成csv
df.to_csv('nba_salaries.csv', index=False)  # 不要左侧的索引