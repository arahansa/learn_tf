
# -*- coding: utf-8 -*-
import tensorflow as tf
sess = tf.Session()

eq = tf.equal([3, 1, 2], 1)
print eq
where = tf.where(eq)
print where
print sess.run(eq)
print sess.run(where)
