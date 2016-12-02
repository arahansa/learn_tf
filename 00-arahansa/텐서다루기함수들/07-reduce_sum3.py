# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

sess = tf.Session()
input3 = np.array([
    [[1,2,3,4], [5,6,7,8], [9,10,11,12]],
    [[13,14,15,16], [17,18,19,20], [21,22,23,24]]
])
print sess.run(tf.reduce_sum(input3))

sum = 0
for i in xrange(25):
    sum = sum + i
print "sum :", sum

print tf.convert_to_tensor(input3)
print "--- 0 차원의 reduce sum --- "
print sess.run(tf.reduce_sum(input3, 0))
print "--- 1 차원의 reduce sum --- "
print sess.run(tf.reduce_sum(input3, 1))
print "--- 2 차원의 reduce sum --- "
print sess.run(tf.reduce_sum(input3, 2))

