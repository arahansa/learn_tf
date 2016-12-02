# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

# 'input' is [[[1, 1, 1], [2, 2, 2]],
#             [[3, 3, 3], [4, 4, 4]],
#             [[5, 5, 5], [6, 6, 6]]]

input = np.array(
    [[[1, 1, 1], [2, 2, 2]],
              [[3, 3, 3], [4, 4, 4]],
              [[5, 5, 5], [6, 6, 6]]
             ])


sess = tf.Session()
print "-------------------------------------"
print "tf.slice(input, [1, 0, 0], [1, 1, 3])"
print "-------------------------------------"
print sess.run(tf.slice(input, [1, 0, 0], [1, 2, 3]))

print "-------------------------------------"
print "tf.slice(input, [1, 0, 0], [1, 2, 3])"
print "-------------------------------------"
print sess.run(tf.slice(input, [1, 0, 0], [1, 2, 3]))