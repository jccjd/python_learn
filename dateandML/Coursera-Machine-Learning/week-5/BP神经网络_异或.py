import numpy as np
import pandas as pd
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
    x_test = X[:20]
    Y = np.array([Y])
    y_test = Y[:20]
    return X, Y, x_test, y_test

def normalization(X):
    xmin, xmax = X.min(), X.max()
    X = (X - xmin) / (xmax - xmin)
    return X

X, Y, x_test, y_test = get_data()
X = normalization(X)
print(X.shape, end='-----')
print(Y.shape, end='------')
#权值初始化，取值范围-1到1
V = np.random.random((5, 20))*2 - 1
W = np.random.random((20, 1))*2 - 1

#学习率设置
lr = 0.1
def sigmoid(x):
    return 1/(1 + np.exp(-x))
#sigmoid的导数
def dsigmoid(x):
    return x*(1-x)
def update():
    global X, Y, W, V, lr
    L1 = sigmoid(np.dot(X, V)) #隐藏层输出（4,4）
    L2 = sigmoid(np.dot(L1, W))#输出层输出（4,1）

    L2_delta = (Y.T - L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)

    W_C = lr * L1.T.dot(L2_delta)
    V_C = lr * X.T.dot(L1_delta)

    W = W + W_C
    V = V + V_C

for i in range(200000):
    update()
    if i % 5000 == 0:
        L1 =sigmoid(np.dot(X, V))
        L2 = sigmoid(np.dot(L1, W))
        print('Error:', np.mean(np.abs(Y.T - L2)))

# 判断是正例还是反例
def judge(x):
    if x > 0.5:
        return 1
    else:
        return 0

# 对数据的前10个进行判断
def prediction(test_data):
    test_data = normalization(test_data)
    L1 = sigmoid(np.dot(test_data, V))
    L2 = sigmoid(np.dot(L1, W))
    result = []
    for i in map(judge, L2):
        result.append(i)
    print(result)

prediction(x_test)
