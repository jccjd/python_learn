import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Solution
condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print(iris_2d[condition])
# > array([[ 4.8,  3.4,  1.6,  0.2],
# >        [ 4.8,  3.4,  1.9,  0.2],
# >        [ 4.7,  3.2,  1.6,  0.2],
# >        [ 4.8,  3.1,  1.6,  0.2],
# >        [ 4.9,  2.4,  3.3,  1. ],
# >        [ 4.9,  2.5,  4.5,  1.7]])

# # 10000个平均分布
# p = np.random.rand(10000)
# plt.hist(p, bins=20, color = 'g', edgecolor='k')
# # 极限中心定律
# N = 10000
# times = 100
# z = np.zeros(N)
# for i in range(times):
#     z += np.random.rand(N)
# z /= times
# plt.hist(z, bins=20, color='m',edgecolor='k')

d = np.random.rand(3, 4)
data = pd.DataFrame(data=d, columns=list('梅兰竹菊'))
print('---'*10)
print(data)
print(data[list('竹菊')])
# pandas 对数据的保存
data.to_csv('data.csv', index = False, header = True)

