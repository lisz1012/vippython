# Author: lisz1012
# Creation date and time: 5/28/24 9:19 PM

scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

print('----------------------')

del scores['张三']  # 删除'张三'这个键值对
print(scores)
scores.clear()  # 清空字典
print(scores)
scores['陈六'] = 98  # 添加元素
print(scores)
scores['陈六'] = 100  # 修改元素
print(scores)
