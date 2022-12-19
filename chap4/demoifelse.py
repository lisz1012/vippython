# Author: lisz1012
# Creation date and time: 12/17/22 8:53 PM

money = 1000
s = int(input("请输入取款金额"))
if s <= money:
    money -= s
    print("取款成功， 余额为:", money)
else:
    print("余额不足，取款失败")