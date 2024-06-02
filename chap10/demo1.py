1  # Author: lisz1012


# Creation date and time: 5/31/24 8:57 PM

# 定义一个函数
def calc(a, b):
    c = a + b
    return c


# 调用函数
res = calc(10, 20)
print(res)

res = calc(b=10, a=20)  # 关键字参数
print(res)

res = calc(10, b=20)  # 位置参数和关键字参数混合使用
print(res)
# res = calc(b=10)
# print(res)
res = calc(10, b=20, c=30)  # 位置参数和关键字参数混合使用, 但是多传了一个参数
print(res)
