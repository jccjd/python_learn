# 基于tensorflow 的 NN ： 用张量表示数据， 用计算图搭建神经网络，用会话执行计算图，优化线上的权重得到模型
import  tensorflow as tf
import numpy as np
#
# a = tf.constant([1.0, 2.0]) # 表示常数，张量只表示运算过程 不表示运算结果
# b = tf.constant([2.0, 2.0])
# print(a + b)# Tensor("add:0", shape=(2,), dtype=float32)
# # 计算图：搭建神经网络的计算过程，只搭建不运算
# x = tf.constant([[1.0, 2.0]])
# y = tf.constant([[3],[4]])
BATCH_SIZE = 8
seed = 23455
rng = np.random.RandomState(seed)
X = rng.rand(32, 2)
Y = [[int(x0 + x1 < 1)] for (x0, x1) in X]
print("x:",X)
print("Y:",Y)

x = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1,seed=1))
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

loss = tf.reduce_mean(tf.square(y - y_))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    # print(sess.run(w1))
    # print(sess.run(w2))

    steps = 300
    for i in range(steps):
        start = (i * BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={
            x: X[start:end],
            y_:Y[start:end]
        })
        if i % 20 == 0:
            pass
            # print(sess.run(loss,feed_dict={x:X, y_:Y}))


    print(sess.run(w1))
    print("*"*10)
    print(sess.run(w2))
