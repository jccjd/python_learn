import numpy as np


data = np.genfromtxt('data1.txt')
print(np.isnan(data))

# ValueError: Input contains NaN, infinity or a value too large for dtype('float64').

##以此来判断数据中是否含有nan值，数据中的异常