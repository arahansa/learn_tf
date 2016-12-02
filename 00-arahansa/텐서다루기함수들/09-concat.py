# -*- coding: utf-8 -*-
import tensorflow as tf
import functions

c1 = tf.constant([1, 3, 5, 7, 9, 0, 2, 4, 6, 8])
c2 = tf.constant([1, 3, 5])
v1 = tf.constant([[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]])
v2 = tf.constant([[1, 2, 3], [7, 8, 9]])

# concat 에 차원을 명시해준다..?

print('-----------concat------------')
functions.showOperation(tf.concat(0, [c1, c2]))     # [1 3 5 7 9 0 2 4 6 8 1 3 5]
functions.showOperation(tf.concat(1, [v1, v2]))     # [[1 2 3 4 5 6 1 2 3] [7 8 9 0 1 2 7 8 9]]