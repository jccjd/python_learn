import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

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

for i in range(10000):
    batch = mnist.train.next_batch(50)
    tran_step.run(feed_dict={x: batch[0],y_:batch[1]})

print(accuracy.eval(feed_dict={x: mnist.test.images, y_:mnist.test.labels}))

