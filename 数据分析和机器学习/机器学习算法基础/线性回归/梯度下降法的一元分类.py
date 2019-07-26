#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
# 载入数据
data = np.genfromtxt("data1.txt",delimiter=",")
x_data = data[:,0]
y_data = data[:,1]
#学习率
lr = 0.01
b, k = 0, 0
#最大迭代次数
epochs = 1000
#最小二乘法
def compute_error(b,k,x_data,y_data):
    totalError = 0
    for i in range(0,len(x_data)):
        totalError += (y_data[i] - (k* x_data[i] + b)) ** 2
    return totalError / float(len(x_data)) / 2.0
def gradient_descent_runner(x_data, y_data, b, k, lr, epochs):
    #计算总数据量
    m = float(len(x_data))
    # 循环epochs次
    for i in range(epochs):
        b_grad = 0
        k_grad = 0
        # 计算梯度的总和再求pingjun
        for j in range(0,len(x_data)):
            b_grad += (1/m) * (((k * x_data[j]) + b) - y_data[j])
            k_grad += (1/m) * (((k * x_data[j]) + b) - y_data[j]) * x_data[j]
        # 更新b 和k
        b = b - (lr * b_grad)
        k = k - (lr * k_grad)
        #每迭代5次，输出一次图形
#         if i % 5 == 0:
#             print("epochs:",i)
#             plt.plot(x_data,y_data,'b.')
#             plt.plot(x_data,k*x_data + b,'r')
#             plt.show()
    return b, k
b, k = gradient_descent_runner(x_data,y_data, b, k, lr, epochs)
print("after{0} iterations b={1}, k = {2},error={3}".format(epochs,b,k, compute_error(b, k ,x_data, y_data)))

plt.plot(x_data,y_data,'b.')
plt.plot(x_data,k*x_data + b,'r')
plt.show()






