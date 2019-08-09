### tensor 
既是张量就是数组,一伴是二维数组
### 构建图
就是将神经网络先构建好，而不做而不做任何的输入

    import tensorflow as tf
    martix1 = tf.constant([[3, 2]])
    martix2 = tf.constant([[2], [2]])
    product = tf.matmul(martix1, martix2)
像这样product是不会被计算的，只有调用了
sess.run()才会打印出最终的结果       

### 在会话中启图
构造完成后，才启动图，启动图的第一步是创建以Session对象，
如果不添加参数，会话构造器会启动默认图,最后要关闭会话

    sess = tf.Session()
    result = sess.run(product)
    print(result)
    sess.close()

一般使用`with`代码块来自动完成关闭动作
    
    with tf.Session() as sess:
        reslut = sess.run(result)
        print(result)   

### 调用GPU 
一般有一块cpu和一块Gpu，不需要指定用什么去计算，tensorflow会找gpu计算
但但有两块以上的话，需要指定用两块， 如果不指定，会默认第一个
    
       with tf.Session() as sess:
        with tf.device("/gpu:1"):
            matrix1 = tf.constant([3,3]])
            matrix2 = tf.constant([2],[2])
            product = tf.matmul(matrix1, matrix2)

设备用字符串进行标识:
- "/cpu:0": 机器的 CPU.
- "/gpu:0": 机器的第一个 GPU, 如果有的话.
- "/gpu:1": 机器的第二个 GPU, 以此类推.


### 一次变量的更新过程

    
    # 变量 初始化标量0
    state = tf.Variable(0, name='counter')
    
    # 创建一个op， 其作用是使state增加1
    one = tf.constant(1)
    new_value = tf.add(state, one)
    update = tf.assign(state, new_value)
    
    # 启动图后，变量必须先去初始化
    init_op = tf.initialize_all_variables()
    # 启动图
    with tf.Session() as sess:
        sess.run(init_op)
        # state的初始值
        print(sess.run(state))
    
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))


在调用可以看到上面的代码为state 值 在执行sess.run()前是不会对state进行改变的
### feed
feed 使用一个 tensor 值临时替换一个操作的输出结果. 你可以提供 feed 数据作为 run() 调用的参数. 
feed 只在调用它的方法内有效, 方法结束,feed 就会消失. 最常见的用例是将某些特殊的操作指定为 "feed" 操作, 
 标记的方法是使用 tf.placeholder() 为这些操作创建占位符.
 
    input1 = tf.placeholder(tf.types.float32)
    input2 = tf.placeholder(tf.types.float32)
    output = tf.mul(input1, input2)
    with tf.Session() as sess:
      print sess.run([output], feed_dict={input1:[7.], input2:[2.]})
      

### mnist
mnist是一个手写数字图片的数据集，一共有7万张图片， 一万的测试集
    
    x = tf.placeholder("float", [None, 784])
`x` 是一个站位的，代表不知道要输入多少的图片，

然后对于定义的权重和偏执，就用Variable,代表一个可以修改的张量，因为因为本来我们就是要不断的
更新权重和偏执的
    
    W = tf.Variable(tf.zeros[[784,10]])
    b = tf.Variable(tf.zeros[10])
    
为什么是`[784,10]`,因为图片的特征是784,最后要的到0-9的分类是10
    
    y = tf.nn.softmax(tf.matmul(x,W)+b)

### 训练模型
一般的代价函数为最小二乘法
- 这里用交叉熵


            
    y_ = tf.placeholder('float',[None,10])
    
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))

- 然后用梯度下降损失函数



    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
- 初始化变量

    
    init = tf.initialize_all_variables()
    
- 启动模型
    
    
    sess = tf.Session()
    sess.run(init)
    
- 训练模型


      for i in range(1000):
          batch_xs, batch_ys = mnist.train.next_batch(100)
          sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

- 评估模型



    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,'float')
    print sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
 `tf.argmx` 可以给一个数组中最大位置的索引，   `tf.cast`则可以将布尔值转换成数字
 
 ### InteractiveSession
 可以有如下操作
 
    import tensorflow as tf
    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    
    sess = tf.InteractiveSession()
    
    x = tf.placeholder("float", shape=[None, 784])
    y_ = tf.placeholder("float", shape=[None, 10])
    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))
    
    sess.run(tf.initialize_all_variables())
    
    y = tf.nn.softmax(tf.matmul(x,W) + b)
    
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    
    tran_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    
    correct_predicttion = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_predicttion, 'float'))
    
    for i in range(1000):
        batch = mnist.train.next_batch(50)
        tran_step.run(feed_dict={x: batch[0],y_:batch[1]})
    
    print(accuracy.eval(feed_dict={x: mnist.test.images, y_:mnist.test.labels}))
    
    print(sess.run(W[10:100]))
    

### 构建一个卷积网络
在模型权重初始化的时候,加入少量噪声来打破对称性避免0梯度

    def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)
    
    def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

