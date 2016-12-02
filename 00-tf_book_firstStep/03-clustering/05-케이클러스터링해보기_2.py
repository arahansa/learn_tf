# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
sess = tf.Session()

# 점 생성
num_points = 2000
vectors_set = []

for i in xrange (num_points):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0, 0.9), np.random.normal(0.0,0.9)])
    else:
        vectors_set.append([np.random.normal(3.0, 0.5), np.random.normal(1.0,0.5)])

print vectors_set


# 그래프 그리기

df = pd.DataFrame({"x":[v[0] for v in vectors_set], "y":[v[1] for v in vectors_set]})
sns.lmplot("x","y", data=df, fit_reg=False, size=6)

vectors = tf.constant(vectors_set)
k=4
centroids = tf.Variable(tf.slice(tf.random_shuffle(vectors),[0,0],[k,-1]))

print "vectors :", vectors
print "centroids:", centroids.get_shape()

expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroids = tf.expand_dims(centroids, 1)
print "vectors :", expanded_vectors
print "centroids:", expanded_centroids.get_shape()
print "---------------------------"
print expanded_vectors.get_shape()
print expanded_centroids.get_shape()
plt.show()