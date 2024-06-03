# Author: lisz1012
# Creation date and time: 6/2/24 3:03 PM

class Person:
    def __new__(cls, *args, **kwargs):  # new方法是创建对象时调用的方法
        print('__new__被调用执行了, cls 的 id 是:', id(cls))  # cls 是类对象Person的id
        obj = super().__new__(cls)
        print('创建的对象的 id 是:', id(obj))
        return obj

    def __init__(self, name, age):  # init方法是初始化对象时调用的方法, 在 new 之后, self 是 new 返回的对象
        print('__init__被调用执行了, self 的 id 是:', id(self))
        self.name = name
        self.age = age


print('Object这个类的id是:', id(object))
print('Person这个类的id是:', id(Person))
p1 = Person('张三', 20)
print('p1这个对象的id是:', id(p1))
