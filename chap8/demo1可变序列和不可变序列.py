# Author: lisz1012
# Creation date and time: 5/29/24 5:49 PM

lst = [10, 20, 45]
print(id(lst))
lst.append(300)
print(id(lst))

s = 'hello'
print(id(s))
s += 'world'
print(id(s))
