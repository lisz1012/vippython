# Author: lisz1012
# Creation date and time: 6/5/24 8:41 PM

height = float(input('请输入身高（cm）：'))
weight = float(input('请输入体重（kg）：'))
bmi = weight / (height / 100) ** 2
print('您的BMI指数为：' + '{:0.2f}'.format(bmi))
if bmi < 18.5:
    print('您的体重过轻。')
elif 18.5 <= bmi < 24:
    print('您的体重正常。')
elif 24 <= bmi < 28:
    print('您的体重过重。')
else:
    print('您的体重肥胖。')
