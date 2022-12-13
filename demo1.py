print(520)
print(3.14)
print("hello world")
print('hello world')
print("""hello world""")
print(3 + 2)

fp = open('/Users/shuzheng/PycharmProjects/vippython/data/text.txt', 'a+') # 表示读写方式打开，如果文件不存在就创建，反之则追加
print("hello", file=fp)
fp.close()

# 不换行输出, 单词之间还有空格
print ('hello', 'world', 'python')