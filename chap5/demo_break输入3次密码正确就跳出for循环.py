# Author: lisz1012
# Creation date and time: 5/27/24 3:57 PM

for item in range(3):
    password = input('Please enter the password: ')  # input()卡在那里，等待用户输入
    if password == '123':
        print('Password correct!')
        break
    print('Password incorrect!')


