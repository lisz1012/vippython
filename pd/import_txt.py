# Author: lisz1012
# Creation date and time: 12/18/22 10:44 PM

import pandas as pd
df = pd.read_csv('rating.txt', sep='\t', encoding='gbk', header=None)
print(df.head())