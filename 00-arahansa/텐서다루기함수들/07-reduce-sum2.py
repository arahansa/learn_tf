# -*- coding: utf-8 -*-
import tensorflow as tf
sess = tf.Session()
X = [1, 2, 3]
Y = [3, 4, 5]

print "pow ", sess.run(tf.pow(tf.sub(X,Y), 2))
print "reduce_sum ", sess.run(tf.reduce_sum(tf.pow(tf.sub(X,Y), 2)))
print "reduce_sum/n", sess.run(tf.reduce_sum(tf.pow(tf.sub(X,Y), 2))/3)
print "reduce_mean/n", sess.run(tf.reduce_mean(tf.pow(tf.sub(X,Y), 2)))



