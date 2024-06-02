# Author: lisz1012
# Creation date and time: 6/1/24 8:13 PM

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名: {0}, 年龄: {1}'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        super().info()
        print('分数: {0}'.format(self.score))


stu = Student('张三', 20, 100)
stu.info()


class Teacher(Person):
    def __init__(self, name, age, teach_of_years):
        super().__init__(name, age)
        self.teach_of_years = teach_of_years

    def info(self):
        super().info()
        print('教龄: {0}'.format(self.teach_of_years))


tea = Teacher('李四', 30, 10)
tea.info()
