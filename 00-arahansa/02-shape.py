# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

# 't' is [[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]]
# shape of tensor 't' is [2, 2, 3]
t = np.array([[[1, 1, 1], [2, 2, 2]],
              [[3, 3, 3], [4, 4, 4]]])
tensor_id = np.array([1.3, 1, 4.0, 23.99])
print "t :", t
tensor = tf.convert_to_tensor(t)
print "========"
sess = tf.Session()
print sess.run(tensor)
