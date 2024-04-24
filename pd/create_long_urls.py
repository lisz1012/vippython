from faker import Faker
import pandas as pd

fake = Faker()

# 创建一个空的集合来存储生成的 URL
urls = set()

# 循环直到我们有 1000 个不重复的 URL
while len(urls) < 1000:
    url = fake.url()
    # 确保 URL 的长度小于 256
    if len(url) < 256:
        urls.add(url)

# 将 URL 集合转换为 DataFrame
df = pd.DataFrame(list(urls), columns=['url'])

# 将 DataFrame 保存为 CSV 文件
df.to_csv('urls.csv', index=False)