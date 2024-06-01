# Author: lisz1012
# Creation date and time: 5/31/24 7:27 PM

s = "hello.python"
print('1. ', s.isidentifier())
print('2. ', 'hello'.isidentifier())
print('3. ', '张三'.isidentifier())
print('4. ', '张三_'.isidentifier())
print('5. ', '张三_123'.isidentifier())
print('6. ', '123'.isidentifier())

print('7. ', '\t'.isspace())
print('8. ', 'abc'.isalpha())
print('9. ', '张三'.isalpha())
print('10. ', '张三1'.isalpha())

print('11. ', '123'.isdecimal())
print('12. ', '123'.isdigit())
print('13. ', '123五'. isdecimal())  # 123五不是阿拉伯数字, 罗马数字也不是阿拉伯数字

print('14. ', '123'.isnumeric())
print('15. ', '123五'.isnumeric())  # True 123五是数字, 但不是阿拉伯数字, 罗马数字也是数字

print('16. ', 'abc123'.isalnum())  # 字母和数字组成
print('17. ', '张三123'.isalnum())  # 字母和数字组成
print('18. ', 'abc!'.isalnum())  # 不是字母和数字组成
