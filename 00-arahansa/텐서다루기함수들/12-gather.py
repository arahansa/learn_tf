
# -*- coding: utf-8 -*-
import tensorflow as tf
import functions
sess = tf.Session()

c1 = tf.constant([1, 3, 5, 7, 9, 0, 2, 4, 6, 8])

c2 = tf.constant([1, 3, 5])

v1 = tf.constant([[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]])

v2 = tf.constant([[1, 2, 3], [7, 8, 9]])


print('-----------gather------------')
print c1
ga = tf.gather(c1, [2, 5, 2, 5])
print ga
functions.showOperation(ga)     # [5 0 5 0]
functions.showOperation(tf.gather(v1, [0, 1]))           # [[1 2 3 4 5 6] [7 8 9 0 1 2]]
functions.showOperation(tf.gather(v1, [[0, 0], [1, 1]])) # [[[1 2 3 4 5 6] [1 2 3 4 5 6]]  [[7 8 9 0 1 2] [7 8 9 0 1 2]]]
