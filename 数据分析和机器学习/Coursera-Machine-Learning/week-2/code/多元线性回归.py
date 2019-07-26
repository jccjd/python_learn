#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[30]:


data = genfromtxt('data2.txt',delimiter=',')
print(data)


# In[31]:


x_data = data[:,:-1]
y_data =data[:,-1]
print(x_data)
print(y_data)


# In[32]:


#学习率
lr = 0.0001
theta1 = 0
theta0 = 0
theta2 = 0
#最大迭代次数
epochs = 1000
#最小二分法
def compute_error(theta0,theta1,theta2,x_data,y_data):
    totalError = 0
    for i in range(0,len(x_data)):
        totalError += (y_data[i] - (theta1*x_data[i,0] + theta2*x_data[i,1] + theta0)) ** 2
    return totalError / float(len(x_data))
def gradient_descent_runner(x_data,y_data,theta0,theta1,theta2,lr,epochs):
    #计算总数量
    m = float(len(x_data))
    #循环epochs
    for i in range(epochs):
        theta0_grad = 0
        theta1_grad = 0
        theta2_grad = 0
        #计算梯度的总和在求平均
        for j in range(0,len(x_data)):
            theta0_grad += (1/m)*((theta1*x_data[j,0]+ theta2*data[j,1]+theta0) - y_data[j])
            theta1_grad += (1/m)*x_data[j,0]*((theta1 * x_data[j,0] + theta2 * x_data[j,1] + theta0) - y_data[j])
            theta2_grad += (1/m)*x_data[j,1]*((theta1 * x_data[j,0] + theta2 * x_data[j,1] + theta0) - y_data[j])
        #更新
        theta0 = theta0 - (lr * theta0_grad)
        theta1 = theta1 - (lr * theta1_grad)
        theta2 = theta2 - (lr * theta2_grad)
    return theta0,theta1,theta2


# In[33]:


print("starting theta0 = {0},theta1 = {1},theta2 = {2},error = {3}".
      format(theta0,theta1,theta2,compute_error(theta0,theta1,theta2,x_data,y_data)))
print("Running...")
theta0,theta1,theta2 = gradient_descent_runner(x_data,y_data,theta0,theta1,theta2,lr,epochs)
print("After theta0 = {0},theta1 = {1},theta2 = {2},error = {3}".
      format(theta0,theta1,theta2,compute_error(theta0,theta1,theta2,x_data,y_data)))


# In[34]:


ax =plt.figure().add_subplot(111,projection = '3d')
ax.scatter(x_data[:,0],x_data[:,1],y_data,c = 'r',marker = 'o',s = 100)#点为红色三角形
x0 = x_data[:,0]
x1 = x_data[:,1]
#生成网格矩阵
x0,x1 = np.meshgrid(x0,x1)
z = theta0 + x0 * theta1 + x1*theta2
ax.plot_surface(x0,x1,z)
#设置坐标轴
# ax.set_xlable('Miles')
# ax.set_ylable('Num of Deliveries')
# ax.set_zlable('Time')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




