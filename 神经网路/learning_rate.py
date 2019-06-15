#coding:utf-8
#设置损失函数 loss = (w+1)^2,令w初值是常数5.反向传播就是求最优w，即求最小loss对应的w值
import tensorflow as tf
#定义待优化函数w初值赋5
w = tf.Variable(tf.constant(5,dtype = tf.float32))
learning_rate = 1
#定义损失函数loss
loss = tf.square(w + 1)
#定义反向传播方法
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
#生成会话，训练40轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(40):
        sess.run(train_step)
        w_val = sess.run(w)
        loss_val = sess.run(loss)
        print("after:",i,"w:",w_val,"loss:",loss_val)
