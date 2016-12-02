# -*- coding: utf-8 -*-
import tensorflow as tf

sess = tf.Session()
# 참고 http://pythonkim.tistory.com/65
c1 = tf.constant([1, 3, 5, 7, 9, 0, 2, 4, 6, 8])
c2 = tf.constant([1, 3, 5])
v1 = tf.constant([[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]])
v2 = tf.constant([[1, 2, 3], [7, 8, 9]])


print sess.run(tf.slice(c1, [2], [3]))            # [5 7 9]


print '---------'
print v1
print sess.run(tf.slice(v1, [0, 2], [2,-1]))       # [[3 4]]

