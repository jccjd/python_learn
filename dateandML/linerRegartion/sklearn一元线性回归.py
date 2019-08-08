from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 载入数据
data = np.genfromtxt('data1.txt', delimiter=',')

x_data = data[:,0,np.newaxis]
y_data = data[:,1,np.newaxis]

model = LinearRegression().fit(x_data, y_data)
predicty = model.predict(x_data)


plt.plot(x_data, y_data, 'b.')
plt.plot(x_data,predicty,'r')
plt.show()