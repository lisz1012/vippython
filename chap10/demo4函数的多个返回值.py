# Author: lisz1012
# Creation date and time: 5/31/24 9:39 PM

def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 调用函数, 获取多个返回值, 使用元组做多个变量的接收
(odd, even) = fun([10, 21, 30, 35, 40, 55, 60, 75])
print('奇数:', odd)
print('偶数:', even)
