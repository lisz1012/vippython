# Author: lisz1012
# Creation date and time: 6/1/24 9:27 PM

print(dir(object))  # 查看object类的所有属性和方法
print('--' * 20)


class A:
    def info(self):
        print('A中的info方法')


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.__age = age


class D(A):
    pass


print(dir(C))  # 查看C类的所有属性和方法, 包括继承下来的和私有属性
c = C('张三', 20)
print(dir(c))  # 查看c对象的所有属性和方法, 包括继承下来的和私有属性
print(c.__dict__)  # 查看c对象的属性字典, 该字典中包括私有属性
print(c.__class__.__dict__)  # 查看C类的属性字典
print(C.__dict__)  # 查看C类的属性字典, 与上一句等价, 相当于 java 中的 类.class和对象.getClass()
print('--' * 20)
print(C.__bases__)  # 查看C类的基类元组(直接父类, 所以不包括object类)
print(A.__bases__)  # 查看A类的父类
print(B.__bases__)  # 查看B类的父类
print(C.__base__)  # 查看C类的父类(第一个父类)
print(C.__mro__)  # 查看C类的继承顺序元组
print(A.__subclasses__())  # 查看A类的所有子类, 是一个列表
