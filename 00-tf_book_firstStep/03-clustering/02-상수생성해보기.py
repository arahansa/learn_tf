# -*- coding: utf-8 -*-
import tensorflow as tf

sess = tf.Session()
print sess.run(tf.fill([2, 3], 9))
print sess.run(tf.constant([1, 2, 3, 4, 5, 6, 7]))
print sess.run(tf.constant(-1.0, shape=[2, 3]))
