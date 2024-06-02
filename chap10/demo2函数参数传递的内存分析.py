# Author: lisz1012
# Creation date and time: 5/31/24 9:15 PM

def fun(arg1, arg2):
    print('arg1, arg2:', arg1, arg2)
    arg1 = 100  # 修改arg1的值, 并不会影响到n1, 只是改了 arg1 的引用指向
    arg2.append(10)
    print('arg1, arg2:', arg1, arg2)


n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print('n1, n2:', n1, n2)
