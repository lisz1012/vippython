# Author: lisz1012
# Creation date and time: 6/5/24 8:56 PM
def fun():
    num = int(input('请输入一个十进制整数：'))
    print(num, '的二进制为:', bin(num))
    print(str(num) + '的二进制为:', bin(num))
    print(f'{num}的二进制为:', bin(num))
    print(f'{num}的二进制为: {bin(num)}')
    print('%s的二进制为:' % num, bin(num))
    print('{0}的二进制为:{1}'.format(num, bin(num)))
    print('---------------------------------')
    print(f'{num}的八进制数为: {oct(num)}')
    print(f'{num}的十六进制数为: {hex(num)}')


if __name__ == '__main__':
    while True:
        try:
            fun()
        except ValueError:
            print('输入错误，请重新输入')
        else:
            break

