# Author: lisz1012
# Creation date and time: 5/28/24 9:37 PM
d = {'name': '张三', 'name': '李四'}  # key重复, 后一个key-value对会覆盖前一个
print(d)  # {'name': '李四'}
d = {'name': '张三', 'nickname': '张三'}  # value重复, 不影响
print(d)  # {'name': '张三', 'nickname': '张三'}
