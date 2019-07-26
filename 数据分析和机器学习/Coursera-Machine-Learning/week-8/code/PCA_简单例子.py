import numpy as np
import matplotlib.pyplot as plt
#载入数据
data = np.genfromtxt('data2.txt',delimiter=',')
x_data =data[:,0]
y_data =data[:,1]
plt.scatter(x_data,y_data)
# plt.show()
#数据中心化
def zeroMean(dataMat):
    #按列求平均，即各个特征的平均
    meanVal = np.mean(dataMat, axis=0)
    newData = dataMat - meanVal
    return newData,meanVal


newData,meanVal = zeroMean(data)
#np.cov用于求协方差矩阵，参数rowvar = 0 说明数据一行代表一个样本
covMat = np.cov(newData,rowvar=0)
covMat
#np.linalg.eig求矩阵的特征值和特征向量
eigVals,eigVects = np.linalg.eig(np.mat(covMat))

#特征值
eigVals

#对特征值从小到大排序
eigValIndice = np.argsort(eigVals)
eigValIndice

top = 1
#最大的top个特征值的下标
n_eigValIndice = eigValIndice[-1:-(top + 1 ):-1]

n_eigValIndice
#最大的n个特征值对应的特征向量
n_eigVect = eigVects[:,n_eigValIndice]
#低维度特征空间对应的特征向量
lowDDataMat = newData*n_eigVect
# print(lowDDataMat)
#利用低维度数据来重构数据
reconMat = (lowDDataMat*n_eigVect.T) + meanVal

#重构的数据画图
x_data = np.array(reconMat)[:,0]
y_data = np.array(reconMat)[:,1]
plt.scatter(x_data,y_data,c='r')
plt.show()