# Author: lisz1012
# Creation date and time: 5/28/24 9:33 PM

scores = {'张三': 100, '李四': 98, '王五': 45}
# 遍历字典
for elem in scores:  # elem是键
    print(type(elem))  # <class 'str'>
    print(type(scores[elem]))  # <class 'int'>
    print(elem, scores[elem])  # 输出键值对
