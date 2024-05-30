# Author: lisz1012
# Creation date and time: 5/27/24 7:33 PM

# 打印乘法表
for i in range(1, 10):  # 1~9
    for j in range(1, i + 1):
        print(i,'*',j,'=',i*j, end='\t')
    print()
