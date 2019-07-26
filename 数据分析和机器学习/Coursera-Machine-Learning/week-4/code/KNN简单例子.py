import matplotlib.pyplot as plt
import numpy as np
import operator

#已知分类数据
x1 = np.array([3,2,1])
y1 = np.array([104,100,81])
x2 = np.array([101,99,98])
y2 = np.array([10,5,2])
scatter1 = plt.scatter(x1,y1,c = 'r')
scatter2 = plt.scatter(x2,y2,c = 'b')
#未知数据
x = np.array([18])
y = np.array([90])
scatter3 = plt.scatter(x,y,c = 'k')
plt.legend(handles=[scatter1,scatter2,scatter3],labels=['labelA','labelB','x'],loc='best')
plt.show()

#已知分类的数据
x_data = np.array([[3,104],
                   [2,100],
                   [101,10],
                   [99,5],
                   [8,2]])
y_data = np.array(['A','A','A','B','B','B'])
x_test = np.array([18,90])
#计算样本数量
x_data_size = x_data.shape[0]
print(x_data_size)
#复制x_test
np.tile(x_test,(x_data_size,1))
#计算x_test与每一个样本的差值
diffMat = np.tile(x_test,(x_data_size,1)) - x_data
print(diffMat)

sqDiffMat = diffMat ** 2
print(sqDiffMat)

#求和
sqDistances = sqDiffMat.sum(axis=1)
print(sqDistances)
#开方
distances = sqDistances ** 0.5
print(distances)
#从小到大排序
sortedDistances = distances.argsort()
print(sortedDistances)

classCount={}
#设置k
k = 5
for i in range(k):
    #获取标签
    votelabel = y_data[sortedDistances[i]]
    classCount[votelabel] = classCount.get(votelabel,0) + 1
print(classCount)

sortedClasscount = sorted(classCount.items(),key=operator.itemgetter(1),reverse = True)
print(sortedClasscount)

#获取数量最多的标签
knncless = sortedClasscount[0][0]
print(knncless)

