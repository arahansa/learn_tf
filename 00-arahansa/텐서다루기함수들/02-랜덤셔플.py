# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

# 점 생성
num_points = 2000
vectors_set = []

for i in xrange (num_points):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0, 0.9), np.random.normal(0.0,0.9)])
    else:
        vectors_set.append([np.random.normal(3.0, 0.5), np.random.normal(1.0,0.5)])

vectors = tf.constant(vectors_set)

sess = tf.Session()

print vectors
print tf.random_shuffle(vectors)

print "---"
print sess.run(vectors)
print "---2---"
print sess.run(tf.random_shuffle(vectors))