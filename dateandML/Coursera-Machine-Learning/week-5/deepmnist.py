import tensorflow as tf
import pandas as pd
import numpy as np

# 将数据转换成两个数组, 训练数据和
def get_data():
    '''
    训练数据: X
    和标签 : Y
    :return: X, Y
    '''

    data = pd.read_excel('data.xlsx')
    type_map = {
        'T恤': 1,
        '衬衫': 2,
        '卫衣/绒衫': 3,
        '连衣裙': 4,
        '半身裙': 5,
    }
    # 将类别替换成数据
    data['类目'] = data['类目'].map(type_map)

    x = data.iloc[:, :-1]
    Y = data.iloc[:, -1]

    X = np.array(x)
    Y = np.array(Y)

    return X, Y

# 均值归一化
def normalization(X):
    xmin, xmax = X.min(), X.max()
    X = (X - xmin) / (xmax - xmin)
    return X

X, Y = get_data()

import math
import random
import pandas as pd

flowerLables = {0: 'Iris-setosa',
                1: 'Iris-versicolor',
                2: 'Iris-virginica'}

random.seed(0)


# 生成区间[a, b)内的随机数
def rand(a, b):
    return (b - a) * random.random() + a


# 生成大小 I*J 的矩阵，默认零矩阵
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


# 函数 sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


# 函数 sigmoid 的导数
def dsigmoid(x):
    return x * (1 - x)


# 定义神经网络类
class NN:
    """ 三层反向传播神经网络 """

    def __init__(self, ni, nh, no):

        # 输入层、隐藏层、输出层的节点（数）
        self.ni = ni + 1  # 增加一个偏差节点bias
        self.nh = nh + 1
        self.no = no

        # 激活神经网络的所有节点（向量）
        self.ai = [1.0] * self.ni
        self.ah = [1.0] * self.nh
        self.ao = [1.0] * self.no

        # 建立权重（矩阵）
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)

        # 设为随机值
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)  # 生成[-0.2,0.2]之间的随机数
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2, 2)  ##生成[-2,2]之间的随机数

    def update(self, inputs):
        # if len(inputs) != self.ni - 1:
        #     raise ValueError('与输入层节点数不符！')

        # 激活输入层
        for i in range(self.ni - 1):
            self.ai[i] = inputs[i]

        # 激活隐藏层
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # 激活输出层
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]

    def backPropagate(self, targets, lr):
        """ 反向传播 """

        # 计算输出层的误差
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k] - self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # 计算隐藏层的误差
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # 更新输出层权重
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] = self.wo[j][k] + lr * change

        # 更新输入层权重
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] = self.wi[i][j] + lr * change

        # 计算误差
        error = 0.0

        ''' 取期望输出和实际输出之差的平方和为误差函数'''
        error += 0.5 * (targets[k] - self.ao[k]) ** 2  # 平方误差函数
        return error

    def test(self, patterns):
        count = 0
        for p in patterns:
            # 原始类别
            target = flowerLables[(p[1].index(1))]
            result = self.update(p[0])

            # 最大值的索引即为预测的类别flowerLables[index]
            index = result.index(max(result))
            print(p[0], ':', target, '->', flowerLables[index])

            # 预测类别和原始类别相同时加1
            count += (target == flowerLables[index])

        # 计算测试准确率
        accuracy = float(count / len(patterns))
        print('accuracy: %-.9f' % accuracy)

    def weights(self):
        print('输入层权重:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('输出层权重:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=1000, lr=0.1):
        # lr: 学习速率(learning rate)
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, lr)
            # 每隔100次输出一次误差
            if i % 100 == 0:
                print('error: %-.9f' % error)


def normalization(X):
    xmin, xmax = X.min(), X.max()
    X = (X - xmin) / (xmax - xmin)
    return X


def iris():
    data = []
    # 读取数据
    data, y = get_data()
    print(len(data))
    data = normalization(data)
    # 随机打乱数据
    random.shuffle(data)
    # 选取打乱后的前100个作为训练数据
    training = data[0:200]
    # 选取打乱后的后50个作为测试数据
    test = data[201:]
    # 输入层4个节点，隐藏层7个，输出层3个(100,010,001三类)
    nn = NN(5, 7, 2)
    # 训练网络，轮10000次
    nn.train(training, iterations=10000)
    # 测试数据
    nn.test(test)



if __name__ == '__main__':
    iris()