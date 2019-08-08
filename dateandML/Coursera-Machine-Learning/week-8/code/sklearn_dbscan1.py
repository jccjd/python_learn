import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
#载入数据
data = np.genfromtxt('data1.txt',delimiter=' ')

#训练模型
model = DBSCAN(eps=1.5,min_samples=4)
model.fit(data)

result = model.fit_predict(data)
# print(result)

#画点
mark = ['or','ob','og','oy','ok']
for i,d in enumerate(data):
    plt.plot(d[0],d[1],mark[result[i]])
plt.show()
