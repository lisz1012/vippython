# Author: lisz1012
# Creation date and time: 12/17/22 9:11 PM

answer = input('您是会员吗？y/n')
money = int(input('消费了多少钱💰？'))
if answer == 'y':
    if money >= 200:
        print("打8折：", money*.8)
    elif money >= 100:
        print("打9折:", money*.9)
    else:
        print("不打折:", money)
else:
    if money >= 200:
        print("打95折:", money*.95)
    else:
        print("不打折:", money)