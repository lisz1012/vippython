class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('学生在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(id(stu1))
print(id(stu2))
print('--------仅仅为 stu2 动态绑定性别属性 ---------')
stu2.gender = '男'  # 动态绑定属性!!!!!!!!
print(stu2.gender)
print('--------stu1 和 stu2 的属性列表---------')
print(stu1.__dict__)
print(stu2.__dict__)
# print(stu3.gender)  # AttributeError: 'Student' object has
stu1.eat()
stu2.eat()


def show():
    print('定义在类之外的, 称为函数')


stu1.show = show  # 动态绑定方法!!!!!!!! stu1.show 可以换为 stu1.xxx
stu1.show()
#stu2.show()   # AttributeError: 'Student' object has no attribute 'show'
print(stu1.__dict__)
print(stu2.__dict__)
