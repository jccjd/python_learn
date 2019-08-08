import numpy as np
# 构建向量，向量是

def compterCost(x, y, theta):
    inner = np.power(((x * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(x))

A = np.mat('1 1; 1 1')
B = np.mat('2 2; 2 2')
print(A)
print(B)