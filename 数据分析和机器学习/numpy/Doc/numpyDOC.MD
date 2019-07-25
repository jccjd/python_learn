## 常见的一些操作
#### 对函数用法的查询 

    print(help(numpy.genfromtxt))
####  每个类型都相同
    matrix = numpy.array([[5, 10, 15], [20,24,90]])
    print(vector.shape)
    print(matrix.shape)
    print(vector.dtype)
####  num 多维数组的取行和列
    matrix1 = numpy.array([
        [1,2,3,4],
        [2,4,5,6],
        [3,4,5,6]
    ])
    print(matrix1[:2] # 第三行
    # 这种方式是求一个交集
    print(matrix1[1:3,0:2])
#### 判断某数是否在一个数组当中
    
        
    matrix1 = numpy.array([
        [1,2,3,4],
        [2,4,5,6],
        [3,4,5,6]
    ])
    print(matrix1 ==2)
    # [[False  True False False]
    #  [ True False False False]
    #  [False False False False]]


#### 对数组元素类型转换

    vector = numpy.array(['1.234','2','3'])
    vector = vector.astype(float)
    print(vector)
#### 对数组中的元素求极值

    list = [1,2,3,4,5]
    print(vector.min())
        
#### 对矩阵求和
    
    matrix1 = numpy.array([
        [1,2,3,4],
        [2,4,5,6],
        [3,4,5,6]
     ])
    # 对行求和
    print(matrix1.sum(axis=1))
    # 对列求和
    print(matrix1.sum(axis=0))
#### 生成数列 and 重构数列

    # 生成一个0-11的数列    
    print(numpy.arange(12))
    # 将一个0-11的数列转换为一个 3 X 4的矩阵
    print(numpy.arange(12).reshape(3, 4))
  
#### 初始化矩阵
    np.zeros((3,4))
    