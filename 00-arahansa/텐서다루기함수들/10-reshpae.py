# -*- coding: utf-8 -*-
import tensorflow as tf
import functions
sess = tf.Session()

c1 = tf.constant([1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 3, 7])
v1 = tf.Variable([[1, 2, 3], [7, 8, 9]])

print('-----------reshape------------')
print tf.reshape(c1, [2, -1])
functions.showOperation(tf.reshape(c1, [2, -1]))    # [[1 3 5 7 9 0] [2 4 6 8 3 7]]
print "---"
print tf.reshape(c1, [-1, 3])
functions.showOperation(tf.reshape(c1, [-1, 3]))    # [[1 3 5] [7 9 0] [2 4 6] [8 3 7]]
print "---"
print tf.reshape(v1, [-1])
functions.showOperation(tf.reshape(v1, [-1]))       # [1 2 3 7 8 9]
