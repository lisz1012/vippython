# Author: lisz1012
# Creation date and time: 5/31/24 8:44 PM

s = '天涯共此时'
print(s.encode(encoding='GBK'))  # GBK编码, 一个中文字符占2个字节
print(s.encode(encoding='UTF-8'))  # UTF-8编码, 一个中文字符占3个字节

byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
print(byte.decode(encoding='utf-8'))  # 解码时, 编码方式要和编码时一致
