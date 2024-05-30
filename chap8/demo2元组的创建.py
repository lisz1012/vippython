# Author: lisz1012
# Creation date and time: 5/29/24 5:55 PM

t = ('Python', 'world', 98)
print(t)
print(type(t))  # <class 'tuple'>

t1 = 'Python', 'world', 98
print(t1)
print(type(t1))  # <class 'tuple'>

t2 = tuple(('Python', 'world', 98))
print(t2)
print(type(t2))  # <class 'tuple'>

t3 = ('Python')
print(t3)
print(type(t3))  # <class 'str'>

t4 = ('Python',)
print(t4)
print(type(t4))  # <class 'tuple'>

t5 = tuple(('Python'))
print(t5)  # ('P', 'y', 't', 'h', 'o', 'n')
print(type(t5))  # <class 'tuple'>

t6 = tuple(('Python',))
print(t6)
print(type(t6))  # <class 'tuple'>

t7 = ()
print(t7)
print(type(t7))  # <class 'tuple'>

t8 = tuple()
print(t8)
print(type(t8))  # <class 'tuple'>
