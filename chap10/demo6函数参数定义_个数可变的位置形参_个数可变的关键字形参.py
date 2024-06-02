# Author: lisz1012
# Creation date and time: 6/1/24 3:15 PM

def fun(*args):  # *args表示可变的位置形参, 元组类型, 只能有一个
    print(args)
    print(args[0])


fun(1)
fun(1, 2)
fun(1, 2, 3)


def fun1(**kwargs):  # **kwargs表示可变的关键字形参, 字典类型
    print(kwargs)
    print(kwargs['name'])


fun1(name='张三', age=20)


def fun2(*args1, **kwargs1):
    print(args1)
    print(kwargs1)


# def fun3(**kwargs2, *args2):  # 位置形参必须在关键字形参之前
#     print(kwargs2)