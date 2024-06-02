# Author: lisz1012
# Creation date and time: 6/1/24 4:04 PM

def fun(a, b):
    c = a + b  # a,b,c都是局部变量
    print(c)


name = '张三'
print(name)


def fun2():
    name = '李四'  # 这个name是局部变量
    print(name)   # 李四
    print(globals()['name'])  # 张三


fun2()
print(name)
print('-----------------')


def fun3():
    global name  # 声明name全局变量, 并引入到这个函数中覆盖本地变量
    name = '王五'  # 修改全局变量name的值!!
    print(name)
    global age
    age = 20  # 声明age是全局变量


fun3()
print(name)  # 王五
print(age)  # 20 全局变量age的值在fun3()函数中被声明和赋值
