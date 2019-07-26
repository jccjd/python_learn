import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#载入数据
data = np.genfromtxt('data3.txt',delimiter = ',')
x_data = data[:,0]
y_data = data[:,1]
# print(x_data,y_data)
# plt.scatter(x_data,y_data)
# plt.show()

x_data = x_data[:,np.newaxis]
y_data = y_data[:,np.newaxis]
#创建并拟合线性回归模型 
	# model = LinearRegression()
	# model.fit(x_data,y_data)
	#画图
	# plt.plot(x_data,y_data,'b.')
	# plt.plot(x_data,model.predict(x_data),'r')
	# plt.show()


poly_reg = PolynomialFeatures(degree = 5)
#特征处理
x_poly = poly_reg.fit_transform(x_data)
#定义回归模型
lin_reg = LinearRegression()
#训练模型
lin_reg.fit(x_poly,y_data) 

#画图
plt.plot(x_data,y_data,'b.')

x_test = np.linspace(1,10,100)
x_test = x_test[:,np.newaxis]
x_poly = poly_reg.fit_transform(x_test)
plt.plot(x_test,lin_reg.predict(x_poly),c = 'r')
plt.show()