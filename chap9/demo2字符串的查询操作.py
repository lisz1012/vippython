# Author: lisz1012
# Creation date and time: 5/30/24 5:10 PM

s = 'hello,hello'
print(s.index('lo'))   # 3
print(s.find('lo'))    # 3
print(s.rindex('lo'))  # 9
print(s.rfind('lo'))   # 9
print(s.find('k'))     # -1
print(s.rfind('k'))    # -1
print(s.index('k'))    # ValueError: substring not found
print(s.rindex('k'))   # ValueError: substring not found
