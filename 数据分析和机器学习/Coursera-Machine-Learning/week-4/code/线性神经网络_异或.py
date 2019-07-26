import numpy as np
import matplotlib.pyplot as plt

# 输入数据
X = np.array([[1, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 1, 1, 1, 1, 1]])
# 标签
Y = np.array([-1, 1, 1, -1])
# 权值初始化，3行1列，取值范围-1 到 1
W = (np.random.random(6) - 0.5) * 2

print(W)
# 学习率设置
lr = 0.11
# 神经网络输出
O = 0
#计算迭代次数
n = 0

def update():
    global X, Y, W, lr, n
    n += 1
    O = (np.dot(X, W.T))
    W_C = lr * ((Y - O.T).dot(X)) / int(X.shape[0])
    W = W + W_C


for _ in range(1000):
    update()

# 正样本
x1 = [0, 1]
y1 = [1, 0]
# 负样本
x2 = [0, 1]
y2 = [0, 1]


def calculate(x, root):
    a = W[5]
    b = W[2] + x * W[4]
    c = W[0] + x * W[1] + x * x * W[3]
    if root == 1:
        return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:
        return (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)


xdata = np.linspace(-1, 2)

plt.figure()

plt.plot(xdata, calculate(xdata,1), 'r')
plt.plot(xdata, calculate(xdata,2), 'r')

plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'yo')
plt.show()
