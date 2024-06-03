# 一个 py 文件就是一个模块, 其中可以包含函数, 类, 语句等

def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '吉林'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('{1}岁的学生{0}在吃饭'.format(self.name, self.age))

    @staticmethod
    def method():
        print('我是静态方法')

    @classmethod
    def cm(cls):
        print('类方法')


a = 10
b = 20
print(a + b)
