# Author: lisz1012
# Creation date and time: 6/1/24 9:20 PM

class Animal:
    def eat(self):
        print('动物吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())  # Python 是一门动态语言，只要传入的对象有eat方法，就可以调用, 无需继承
