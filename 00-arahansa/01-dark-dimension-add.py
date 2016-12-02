# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf


def printTensor(tensor):
  print "--------------------------"
  print "Run :", sess.run(tensor)
  print "구조 :", sess.run(tf.shape(tensor))
  print "크기 :", sess.run(tf.size(tensor))
  print "랭크 :", sess.run(tf.rank(tensor))
  print "--------------------------"


t1 = [[1, 2, 3], [4, 5, 6]]
t2 = [[7, 8, 9], [10, 11, 12]]
t3 = tf.concat(0, [t1, t2])
sess = tf.Session()
printTensor(t3)

# concat 해보기
