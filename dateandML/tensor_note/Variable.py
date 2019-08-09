import tensorflow as tf
martix1 = tf.constant([[3, 2]])
martix2 = tf.constant([[2], [2]])
product = tf.matmul(martix1, martix2)

with tf.Session() as sess:
    result = sess.run(product)


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

# feedfeed 使用一个 tensor 值临时替换一个操作的输出结果.
# 你可以提供 feed 数据作为 run() 调用的参数. feed 只在调用它的方法内有效, 方法结束,
# feed 就会消失. 最常见的用例是将某些特殊的操作指定为 "feed" 操作, 标记的方法是使用 tf.placeholder() 为这些操作创建占位符.

