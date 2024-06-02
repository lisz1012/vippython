# Author: lisz1012
# Creation date and time: 6/1/24 5:51 PM

class Student:  # 首字母大写，符合类的命名规范
    native_place = '吉林'  # 直接定义属性，直接写在类里的变量native_place是类属性, 所有对象共享, 每个对象里都有一个native_place属性，但是通过类指针指向的是同一个内存地址

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
    def cm(cls):  # 类方法和静态方法一样，都是属于类的，不是属于实例的,  区别在于cls参数, cls代表类本身, 通过cls可以访问类的属性, 类似反射
        print('我是类方法，因为我使用了classmethod进行修饰')
        print(cls.native_place)
        print('类的元数据信息:\n', cls.__dict__)


# 定义在类外部的函数，称为函数
def drink():
    print('喝水')


print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '北京'
print(stu1.native_place)
print(stu2.native_place)

print('---------类方法的使用方式---------')
Student.cm()
print('---------静态方法的使用方式---------')
Student.method()
