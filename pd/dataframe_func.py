# Author: lisz1012
# Creation date and time: 12/18/22 10:03 PM

import pandas as pd
data = [['小太阳', 320.9,  100],
        ['鼠标',   150,    50],
        ['小刀',   1.5,    200]]
columns = ['名称', '单价', '数量']
df = pd.DataFrame(data=data, columns=columns)
print(df.describe())
print(df.count())
print(df.sum())
print(df.max())
print(df.min())