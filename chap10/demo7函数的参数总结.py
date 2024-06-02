# Author: lisz1012
# Creation date and time: 6/1/24 3:38 PM

def fun(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)


fun(1, 2, 3)
lst = [11, 22, 33]
fun(*lst)  # *lst表示拆包, 将列表中的元素拆包成位置实参
print('-----------------')
fun(a=100, b=200, c=300)
dic = {'a': 111, 'b': 222, 'c': 333}  # 字典中的key必须和形参名一致
fun(**dic)


def fun1(a, b=10):
    print('a = ', a)
    print('b = ', b)


def fun2(*args):  # *args表示个数可变的位置形参, 元组类型, 只能有一个
    print(args)


def fun3(**kwargs):  # **kwargs表示个数可变的关键字形参, 字典类型
    print(kwargs)


fun2(10, 20, 30, 40)
fun3(name='张三', age=20, a=10, b=20)


def fun4(a, b, c, d):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)


fun4(10, 20, 30, 40)
fun4(a=10, b=20, c=30, d=40)
fun4(10, 20, d=40, c=30)  # 位置形参和关键字形参混合使用, 位置形参必须在关键字形参之前


def fun5(a, b, *, c, d):  # *表示c和d是关键字形参, 必须使用关键字传参
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)


# fun5(10, 20, 30, 40)  # TypeError: fun5() takes 2 positional arguments but 4 were given
fun5(10, 20, c=30, d=40)


def fun6(a, b, *, c, d, **args):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)
    print('args = ', args)


def fun6(*args, **dic):
    print('args = ', args)
    print('dic = ', dic)


def fun7(a, b=10, *args, **args2):
    print('a = ', a)
    print('b = ', b)
    print('args = ', args)
    print('args2 = ', args2)
