# -*- coding: utf-8 -*-
import tensorflow  as tf


a = tf.placeholder("int32")
b = tf.placeholder("int32")

y = tf.mul(a,b)
sess = tf.Session()
print "곱하기 결과 : ",sess.run(y, feed_dict={a:3, b:6})

