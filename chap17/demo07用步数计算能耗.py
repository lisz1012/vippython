# Author: lisz1012
# Creation date and time: 6/5/24 9:16 PM

steps = int(input('请输入步数：'))
calories = 0.035 * steps
print('您消耗的热量为：{:0.2f}卡, 即{:0.2f}千卡'.format(calories, calories / 1000))
