# Author: lisz1012
# Creation date and time: 6/1/24 5:16 PM

try:
    a = int(input('请输入被除数:'))
    b = int(input('请输入除数:'))
    res = a / b
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('输入的不是数字')
else:  # else是相对于except的，如果没有异常发生，就执行else中的代码
    print('结果是:', res)


try:
    a = int(input('请输入被除数:'))
    b = int(input('请输入除数:'))
    res = a / b
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('输入的不是数字')
else:  # else是相对于except的，如果没有异常发生，就执行else中的代码
    print('结果是:', res)
finally:
    print('程序结束, 谢谢您的使用')
