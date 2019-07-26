import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report
from sklearn import preprocessing

# 数据是否需要标准化
scale = True
# 载入数据
data = np.genfromtxt('data1.txt', delimiter=',')
x_data = data[:, :-1]
y_data = data[:, -1]


def plot():
    x0 = []
    x1 = []
    y0 = []
    y1 = []
    # 切分不同类型的数据
    for i in range(len(x_data)):
        if y_data[i] == 0:
            x0.append(x_data[i, 0])
            y0.append(x_data[i, 0])
        else:
            x1.append(x_data[i, 0])
            y1.append(x_data[i, 1])
    # 画图
    scatter0 = plt.scatter(x0, y0, c='b', marker='o')
    scatter1 = plt.scatter(x1, y1, c='r', marker='x')
    plt.legend(handles=[scatter0, scatter1], labels=['lable0', 'lable1'], loc='best')


plot()
# plt.show()

# 数据处理，添加偏执值
x_data = data[:, :-1]
y_data = data[:, -1, np.newaxis]

print(np.mat(x_data).shape)
print(np.mat(y_data).shape)
# 给样本添加偏执项
X_data = np.concatenate((np.ones((14, 1)), x_data), axis=1)
print(X_data.shape)


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def cost(xMat, yMat, ws):
    # 按位相乘multiply
    left = np.multiply(yMat, np.log(sigmoid(xMat * ws)))
    right = np.multiply(1 - yMat, np.log(1 - sigmoid(xMat * ws)))
    return np.sum(left + right) / -(len(xMat))


def gradAscent(xArr, yArr):
    if scale == True:
        xArr = preprocessing.scale(xArr)
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    lr = 0.001
    epochs = 10000
    costList = []

    # 计算数据行列数
    # 行代表数据个数，列代表权值个数
    m, n = np.shape(xMat)
    # 初始化权值
    ws = np.mat(np.ones((n, 1)))

    for i in range(epochs + 1):
        h = sigmoid(xMat * ws)
        # 计算误差
        ws_grad = xMat.T * (h - yMat) / m
        ws = ws - lr * ws_grad

        if i % 50 == 0:
            costList.append(cost(xMat, yMat, ws))
    return ws, costList


# 训练模型，得到权值和cost值的变化
ws, costList = gradAscent(X_data, y_data)
print(ws)

if scale == False:
    # 画图决策边界
    plot()
    x_test = [[-4], [3]]
    y_test = (-ws[0] - x_test * ws[1]) / ws[2]
    plt.plot(x_test, y_test, 'k')
    plt.show()

#画图loss 值的变化
x = np.linspace(0,10000,201)
plt.plot(x, costList,c = 'r')
plt.title('Train')
plt.xlabel("Epochs")
plt.ylabel("Cost")
plt.show()

#预测
def predict(x_data,ws):
    if scale == True:
        x_data = preprocessing.scale(x_data)
    xMat = np.mat(x_data)
    ws = np.mat(ws)
    return [1 if x >= 0.5 else 0 for x in sigmoid(xMat * ws)]

predictions = predict(X_data,ws)
print(classification_report(y_data,predictions))