# Author: lisz1012
# Creation date and time: 5/28/24 9:12 PM

scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
print(scores['张三'])
# print(scores['aa'])  # KeyError: 'aa'
print(scores.get('李四'))
print(scores.get('aa'))  # None
print(scores.get('aa', 60))  # 60是默认值, aa 这个键不存在, 返回默认值60
print(scores.get('张三', 60))  # 100, '张三'这个键存在, 返回对应的值100
