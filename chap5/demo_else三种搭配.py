# Author: lisz1012
# Creation date and time: 5/27/24 4:27 PM

for item in range(3):
    pwd = input('Please enter the password: ')
    if pwd == '123':
        print('Password correct!')
        break
    else:
        print('Password incorrect!')
else:  # 循环中没有break时，执行else语句
    print('for: You have tried 3 times, please try again later.')

a = 0
while a < 3:
    pwd = input('Please enter the password: ')
    if pwd == '123':
        print('Password correct!')
        break
    else:
        print('Password incorrect!')
    a += 1
else:
    print('while: You have tried 3 times, please try again later.')
