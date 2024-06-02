# Author: lisz1012
# Creation date and time: 6/1/24 5:16 PM

try:
    a = int(input('请输入被除数:'))
    b = int(input('请输入除数:'))
    res = a / b
    print('结果是:', res)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('输入的不是数字')
print('程序结束')
