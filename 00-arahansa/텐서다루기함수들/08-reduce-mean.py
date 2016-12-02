# -*- coding: utf-8 -*-
import tensorflow as tf
sess = tf.Session()
X = [1., 2., 3.]
Y = [1., 2., 3.]
m = len(X)

W = tf.placeholder(tf.float32)

hypothesis = tf.mul(W, X)
cost = tf.reduce_sum(tf.pow(hypothesis-Y, 2)) / m

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
print  sess.run(cost, feed_dict={W: 2})