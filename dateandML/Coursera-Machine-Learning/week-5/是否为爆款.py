import pandas as pd
import numpy as np
from numpy import exp, array, random, dot

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

    print(x)
    return X, Y

# 均值归一化
def normalization(X):
    xmin, xmax = X.min(), X.max()
    X = (X - xmin) / (xmax - xmin)
    return X


class NeuralNetwork(object):

    # 初始化权重
    def __init__(self):
        random.seed(1)

        self.synaptic_weights = 2 * random.random((5, 1)) - 1

    # 激活函数为Sigmoid
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        # 把输入数据传入神经网络
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

def judge(x):
    if x > 0.5:
        return 1
    else:
        return 0


if __name__ == "__main__":
    X, Y = get_data()
    X = normalization(X)
    neural_network = NeuralNetwork()
    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)
    training_set_inputs = array(X)
    training_set_outputs = array([Y]).T
    # 用训练集对神经网络进行训练
    # 迭代10000次，每次迭代对权重进行微调.

    neural_network.train(training_set_inputs, training_set_outputs, 10000)
    # 输出训练后的参数值，作为对照。
    print("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)
    # 用新样本测试神经网络.
    print("Considering new situation [1, 0, 0] -> ?: ")
    test = array([5, 5, 1, 1, 1])
    test = normalization(test)
    test = neural_network.think(test)
    print(judge(test))
    print(neural_network.think(array([1, 1, 23479, 2334, 7500])))
    print(neural_network.think(array([1, 1, 15908, 1858, 7900])))
    print(neural_network.think(array([5, 5, 389, 13050, 4400])))
    # 0       1   1   23479   2334  7500
    # 1       1   1   15908   1858  7900
    # 2       1   1   13351   1186  7900
    # 3       1   1   12071    948  6900
    # 4       1   1   11249    851  7900
    #         5   5   389

