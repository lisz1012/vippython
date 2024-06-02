# Author: lisz1012
# Creation date and time: 6/1/24 5:51 PM

class Student:  # 首字母大写，符合类的命名规范
    native_place = '吉林'  # 直接定义属性，直接写在类里的变量native_place是类属性

    def __init__(self, name, age):
        self.name = name  # self.name是实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    #  静态方法
    @staticmethod
    def method():  # 不能写self,因为静态方法是属于类的，不是属于实例的
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):  # 类方法和静态方法一样，都是属于类的，不是属于实例的,  区别在于cls参数, cls代表类本身
        print('我是类方法，因为我使用了classmethod进行修饰')


# 定义在类外部的函数，称为函数
def drink():
    print('喝水')


stu1 = Student('张三', 20)
stu1.eat()
print(stu1.name)
print(stu1.age)
print('-----------------')
Student.eat(stu1)  # stu1.eat()等价于Student.eat(stu1)

