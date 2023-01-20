# Author: lisz1012
# Creation date and time: 1/1/23 6:46 PM

a = 1
sum = 0
while a <= 100:
    if not bool(a % 2):   # 0的布尔值为False
       sum += a
    a += 1
print('1-100之间的偶数和', sum)