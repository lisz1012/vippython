# Author: lisz1012
# Creation date and time: 6/2/24 2:50 PM

a = 20
b = 100
c = a + b  # 底层是调用了int类的__add__方法
print(c)
d = a.__add__(b)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

print(stu1 + stu2)  # 如果上面没重写__add__(), 就会报错 TypeError
print(stu1.__add__(stu2))
print('-----------------')
lst = [11, 22, 33, 44]
print(len(lst))  # 底层是调用了list类的__len__方法
print(lst.__len__())  # 直接调用list类的__len__方法
print(len(stu1))  # 如果上面没重写__len__(), 就会报错 TypeError: object of type 'Student' has no len()
