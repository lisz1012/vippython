# Author: lisz1012
# Creation date and time: 12/17/22 9:22 PM
a = int(input("请输入第一个整数"))
b = int(input("请输入第二个整数"))
if a >= b:
    print(a, "大于等于", b)
else:
    print(a, "小于", b)

print("使用条件表达式")
print(str(a) + "大于等于" + str(b) if a >= b else str(a) + "小于" + str(b))