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

# 1차원의 수
number = 1
dimension1 = tf.convert_to_tensor(number, dtype=tf.float64)

# 2차원으로 변환
dimension2 = tf.expand_dims(dimension1, 0)
# 3차원으로 변환
dimension3 = tf.expand_dims(dimension2, 0)


t = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
dim1_nine = tf.convert_to_tensor(t)

sess = tf.Session()
printTensor(dimension1)
print "2차원 shape 얻기", dimension2.get_shape()
printTensor(dimension2)
printTensor(dimension3)
print "3차원 shape 얻기", dimension3.get_shape()
printTensor(dim1_nine)