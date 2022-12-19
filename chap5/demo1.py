# Author: lisz1012
# Creation date and time: 12/18/22 3:54 PM

r = range(10) # 默认从0开始默认步长为1, 用到的时候现场计算下一个该是谁了
print(r)
print(list(r))

r = range(1,10)
print(list(r))

r = range(1, 10, 3)
print(list(r))

print(10 in r)
print(8 not in r)