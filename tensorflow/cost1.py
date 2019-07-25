#coding:utf-8
#两层简单神经网络
import tensorflow as tf
import numpy as np
seed = 23455
BATCH_SIZE = 8

rng = np.random.RandomState(seed)
X = rng.rand(32,2)
Y_ = [[x1 + x2 + (rng.rand()/10.0 - 0.05)] for (x1,x2) in X]

#定义神经网络的输入，参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32,shape=(None,2))
y_ = tf.placeholder(tf.float32,shape=(None,1))
w1 = tf.Variable(tf.random_normal([2,1],stddev = 1, seed = 1))
y = tf.matmul(x,w1)

#2定义损失函数及反向传播方法
loss = tf.reduce_mean(tf.square(y_ - y))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

#用会话计算结果#3训练steps轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    STEPS = 20000
    for i in range(STEPS):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step,feed_dict={x: X[start:end],y_: Y_[start:end]})
        if i % 500 == 0:
            print("After %d traning steps,w1 is:",(i))
            print(sess.run(w1),"\n")

    print("Final w1 is:\n",sess.run(w1))
