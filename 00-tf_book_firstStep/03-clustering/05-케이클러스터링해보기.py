# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import functions

sess = tf.Session()
# 점 생성
num_points = 20
vectors_set = []

for i in xrange (num_points):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0, 0.9), np.random.normal(0.0,0.9)])
    else:
        vectors_set.append([np.random.normal(3.0, 0.5), np.random.normal(1.0,0.5)])

print vectors_set
vectors = tf.constant(vectors_set)
print vectors

shuffle = tf.random_shuffle(vectors)


