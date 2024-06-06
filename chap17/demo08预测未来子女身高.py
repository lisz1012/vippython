# Author: lisz1012
# Creation date and time: 6/5/24 10:44 PM

father_height = float(input('请输入父亲的身高（cm）：'))
mother_height = float(input('请输入母亲的身高（cm）：'))
son_height = (father_height + mother_height) * 0.54
daughter_height = (father_height + mother_height) * 0.46
print('预测儿子的身高为：' + '{:0.2f}'.format(son_height) + 'cm')
print('预测女儿的身高为：' + '{:0.2f}'.format(daughter_height) + 'cm')
