# Author: lisz1012
# Creation date and time: 6/1/24 9:06 PM

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是: {0}, 我的年龄是: {1}'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu.__str__())  # 类似 java 的 toString() 方法
print(stu)  # 默认调用__str__方法
print(type(stu))  # 默认调用__str__方法
