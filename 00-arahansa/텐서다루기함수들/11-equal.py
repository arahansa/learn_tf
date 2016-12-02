# -*- coding: utf-8 -*-
import tensorflow as tf
import functions
sess = tf.Session()


t1 = tf.constant("1")
t2 = tf.constant("2")
t3 = tf.constant("1")

e1 = tf.equal(t1,t2)
e2 = tf.equal(t1,"1")

print e1
print "e1 : ", sess.run(e1)

print e2
print "e2 : ", sess.run(e2)