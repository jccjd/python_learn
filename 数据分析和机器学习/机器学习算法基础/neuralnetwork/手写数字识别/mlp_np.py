import tensorflow as tf
import urllib
from  tensorflow.examples.tutorials.mnist  import  input_data
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

#建立BP神经网络模型

num_classes = 10 # 数据类型0-9
input_size = 784 # 28*28
hidden_units_size = 30 # 层节点数
batch_size = 100 #
training_iterations = 1000 # 迭代次数

# 设置变量
X = tf.placeholder (tf.float32, shape = [None, input_size])
Y = tf.placeholder (tf.float32, shape = [None, num_classes])

W1 = tf.Variable (tf.random_normal ([input_size, hidden_units_size],
                                    stddev = 0.1))#hidden_units_size = 30#正态分布随机数
B1 = tf.Variable (tf.constant (0.1),
                  [hidden_units_size])#常数为1，形状为（1,1）
W2 = tf.Variable (tf.random_normal ([hidden_units_size,
                                     num_classes], stddev = 0.1))#正态分布随机数
B2 = tf.Variable (tf.constant (0.1), [num_classes])
# 搭建计算网络 使用 relu 函数作为激励函数 这个函数就是 y = max (0,x) 的一个类似线性函数 拟合程度还是不错的
# 使用交叉熵损失函数 这是分类问题例如 ： 神经网络 对率回归经常使用的一个损失函数
#第1层神经网络
hidden_opt = tf.matmul (X, W1) + B1#矩阵运算
hidden_opt = tf.nn.relu (hidden_opt)#激活函数
#第2层神经网络
final_opt = tf.matmul (hidden_opt, W2) + B2#矩阵运算
final_opt = tf.nn.relu (final_opt)#激活函数,最终的输出结果

loss = tf.reduce_mean (
    tf.nn.softmax_cross_entropy_with_logits (labels = Y, logits = final_opt))#损失函数,交叉熵方法


opt = tf.train.GradientDescentOptimizer (0.1).minimize (loss)

init = tf.global_variables_initializer ()#全局变量初始化

correct_prediction = tf.equal (tf.argmax (Y, 1), tf.argmax (final_opt, 1))

accuracy = tf.reduce_mean (tf.cast (correct_prediction, 'float'))#将张量转化成float

# 进行计算 打印正确率
sess = tf.Session ()#生成能进行TensorFlow计算的类
sess.run (init)
for i in range (training_iterations) :
    batch = mnist.train.next_batch (batch_size)#每次迭代选用的样本数100
    batch_input = batch[0]
    batch_labels = batch[1]
    training_loss = sess.run ([opt, loss], feed_dict = {X: batch_input, Y: batch_labels})
    if (i+1) % 100 == 0 :
        train_accuracy = accuracy.eval (session = sess, feed_dict = {X: batch_input,Y: batch_labels})
        print ("step : %d, training accuracy = %g " % (i+1, train_accuracy))

###测试集输出结果可视化

def res_Visual(n):
    #sess=tf.Session()
    #sess.run(tf.global_variables_initializer())

    final_opt_a=tf.argmax (final_opt, 1).eval(session=sess,feed_dict = {X: mnist.test.images,Y: mnist.test.labels})

    fig, ax = plt.subplots(nrows=int(n/5),ncols=5 )

    ax = ax.flatten()

    print('前{}张图片预测结果为：'.format(n))

    for i in range(n):
        print(final_opt_a[i],end=',')
        if int((i+1)%5) ==0:
            print('\t')
        #图片可视化展示
        img = mnist.test.images[i].reshape((28,28))#读取每行数据，格式为Ndarry
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')#可视化

    print('测试集前{}张图片为：'.format(n))
res_Visual(30)