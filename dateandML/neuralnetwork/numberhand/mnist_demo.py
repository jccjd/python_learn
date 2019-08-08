import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
import matplotlib.pyplot as plt
# 初始化
num_classes = 10
input_size = 784
hidden_units_size = 30
batch_size = 100
training_iterations = 2000

# 对x,y赋None值站位
X = tf.placeholder(tf.float32, shape=[None, input_size])
Y = tf.placeholder(tf.float32, shape=[None, num_classes])

# 对权值 和偏置进行初始化
W1 = tf.Variable(tf.random_normal([input_size, hidden_units_size], stddev=0.1, ))

W2 = tf.Variable(tf.random_normal([hidden_units_size, num_classes], stddev=0.1, ))

B1 = tf.Variable(tf.constant(0.1), [hidden_units_size])
B2 = tf.Variable(tf.constant(0.1), [num_classes])

"""前向传播"""
# 隐藏层的权值输出计算 x -> h1
hidden_opt = tf.matmul(X, W1) + B1
hidden_opt = tf.nn.relu(hidden_opt)

# 输出层
final_opt = tf.matmul(hidden_opt, W2) + B2
# 通过激活函数最终输出结果
final_opt = tf.nn.relu(final_opt)

# 交叉熵计算损失函数
loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=final_opt)
)

opt = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

correct_prediction = tf.equal(tf.arg_max(Y, 1), tf.argmax(final_opt, 1))

# 将 true false 转换为 0, 1 并计算平均
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

"""backforward"""
sess = tf.Session()
sess.run(init)
for i in range(training_iterations):
    batch = mnist.train.next_batch(batch_size)
    batch_input = batch[0]
    batch_layers = batch[1]

    training_loss = sess.run([opt, loss], feed_dict= {
        X: batch_input,
        Y: batch_layers
    })
    if (i + 1) % 100 == 0:
        train_accuracy = accuracy.eval(session=sess, feed_dict={
            X: batch_input,
            Y: batch_layers
        })
        print(f"{i} step: ", train_accuracy)

def res_Visual(n):
    final_opt_a = tf.argmax(final_opt, 1).eval(
        session=sess, feed_dict={
            X:mnist.test.images,
            Y: mnist.test.labels
        }
    )
    fig, ax = plt.subplots(nrows=int(n / 5), ncols=5)
    ax = ax.flatten()
    print(format(n))
    for i in range(n):
        print(final_opt_a[i], end=',')
        if int((i + 1) % 5) == 0:
            print('\t')

        img = mnist.test.images[i].reshap((28,28))
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')