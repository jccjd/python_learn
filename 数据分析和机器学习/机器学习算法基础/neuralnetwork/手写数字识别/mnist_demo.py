import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)

# 初始化
num_classes = 10 #
input_size = 784
hidden_units_size = 30
batch_size = 100
traning_iterations = 2000

#对x,y赋None值站位
X = tf.placeholder(tf.float32, shape=[None, input_size])
Y = tf.placeholder(tf.float32, shape=[None, num_classes])

#对权值 和偏置进行初始化
W1 = tf.Variable(tf.random_normal([input_size, hidden_units_size], stddev = 0.1,))

W2 = tf.Variable(tf.random_normal([hidden_units_size, num_classes], stddev = 0.1,))

B1 = tf.Variable(tf.constant(0.1), [hidden_units_size])
B2 = tf.Variable(tf.constant(0.1), [num_classes])

"""前向传播"""
#隐藏层的权值输出计算 x -> h1
hidden_opt = tf.matmul(X, W1) + B1
hidden_opt = tf.nn.relu(hidden_opt)

#
