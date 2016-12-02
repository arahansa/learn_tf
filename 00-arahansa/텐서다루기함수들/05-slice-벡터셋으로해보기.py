# -*- coding: utf-8 -*-
import tensorflow as tf
import functions
sess =tf.Session()

v1 = tf.constant([
    [1,2,4],
    [2,3,6],
    [3,4,7],
    [5,6,8],
    [3,4,9],
    [6,5,10]
])

print v1
functions.showConstant(v1)

print "--- slice ---"
functions.showConstant(tf.slice(v1, [0,0], [3, -1]))

