import functions

import tensorflow as tf
import functions

c1, c2, c3 = tf.constant([1, 2]), tf.constant([1.0, 2.0]), tf.constant([1])
v1, v2 = tf.Variable([1, 3]), tf.Variable([1.0, 3.0])

print('-----------equal------------')
functions.showOperation(tf.equal(c1, v1))           # [ True False]