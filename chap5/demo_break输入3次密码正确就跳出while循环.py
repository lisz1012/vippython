# Author: lisz1012
# Creation date and time: 5/27/24 4:01 PM

a = 0
while a < 3:
    password = input('Please enter the password: ')
    if password == '123':
        print('Password correct!')
        break
    print('Password incorrect!')
    a += 1
