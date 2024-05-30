# Author: lisz1012
# Creation date and time: 5/27/24 3:27 PM

# with this one from chap5/demo_for.py:
for item in 'Python':
    print(item)

# 0 ~ 9
for i in range(10):
    print(i)

# 如果再循环体重不需要使用自定义变量，可以使用下划线代替
for _ in range(5):
    print('Hello, Python!')

# for 循环计算 1-100 之间的偶数和
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)



