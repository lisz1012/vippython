# Author: lisz1012
# Creation date and time: 6/1/24 7:58 PM

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand}牌的汽车已启动...')


car = Car('华为')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性前面有__, 不会在类的外面被使用

    def study(self):
        print(f'{self.name}正在学习...')

    def show(self):
        print(self.name, self.__age)


stu= Student('张三', 20)
stu.study()
print(stu.name)
# print(stu.__age)  # AttributeError: 'Student' object has no attribute '__age'
stu.show()
# 强行访问私有属性
print(dir(stu))
print(stu.__dict__['_Student__age'])  # 20
print(stu._Student__age)  # 20
