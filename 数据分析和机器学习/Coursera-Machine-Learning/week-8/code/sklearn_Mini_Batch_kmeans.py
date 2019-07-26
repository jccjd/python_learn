from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.pyplot as plt

# 载入数据
data = np.genfromtxt('data1.txt', delimiter=' ')
x_data = data[:,0]
y_data = data[:,1]
plt.scatter(x_data,y_data)
plt.show()

# 设置k值
k = 4
# 训练模型
model = MiniBatchKMeans(n_clusters=k)
model.fit(data)
#分类中心点坐标
centers = model.cluster_centers_
print(centers)
#预测结果
result = model.predict(data)


#画图
mark = ['or','ob','og','oy']
for i,d in enumerate(data):
    plt.plot(d[0],d[1],mark[result[i]])

#画出各个分类的中心
mark = ['*y','*g','*b','*r']
for i, centers in enumerate(centers):
    plt.plot(centers[0],centers[1],mark[i],markersize = 20)

#画出簇的作用域
x_min,x_max = data[:,0].min() - 1,data[:,0].max() + 1
y_min,y_max = data[:,1].min() - 1,data[:,1].max() + 1


#生成网格矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min,y_max,0.02))

z = model.predict(np.c_[xx.ravel(),yy.ravel()])
z = z.reshape(xx.shape)
#等高线图
cs = plt.contourf(xx,yy,z)
#显示结果
# plt.show()