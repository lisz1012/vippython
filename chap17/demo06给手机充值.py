# Author: lisz1012
# Creation date and time: 6/5/24 9:10 PM

balance = 8
print('用户手机原有话费金额为 \033[0:35m{0}\033[m 元'.format(balance))
recharge = int(input('请输入充值金额：'))
balance += recharge
print('用户手机充值后话费金额为 \033[0:32m{0}\033[m 元'.format(balance))
