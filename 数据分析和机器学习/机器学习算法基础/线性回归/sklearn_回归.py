import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#读入数据
data = genfromtxt('data2.txt',delimiter = ',')
print(data)


#切分数据
x_data = data[:,:-1]
y_data = data[:,-1]
print(x_data)
print(y_data)

#创建model
model = linear_model.LinearRegression()
model.fit(x_data,y_data)

# 系数
print("coefficients:",model.coef_)
#截距
print('intercept:',model.intercept_)
#测试
x_test = [[102,4]]
predict = model.predict(x_test)
print("predict",predict)

#画3d图
ax = plt.figure().add_subplot(111,projection = '3d')
ax.scatter(x_data[:,0],x_data[:,1],y_data,c = 'r',marker = 'o',s = 100)#点为红色三角形
x0 = x_data[:,0]
x1 = x_data[:,1]
#生成网格矩阵
x0,x1 = np.meshgrid(x0,x1)
z = model.intercept_ + x0 * model.coef_[0] + x1 * model.coef_[1]
#画3d图
ax.plot_surface(x0,x1,z)
plt.show()
