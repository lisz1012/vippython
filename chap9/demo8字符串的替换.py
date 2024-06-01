# Author: lisz1012
# Creation date and time: 5/31/24 7:43 PM

s = 'hello,python'
print(s.replace('python', 'java'))
s1 = 'hello, python, python, python'
print(s1.replace('python', 'java', 2))

lst = ['hello', 'world', 'python']
print(' '.join(lst))
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'world', 'python')
print(' '.join(t))
print('|'.join(t))
print(''.join(t))

print('*'.join('hello'))
