# -*- coding: utf-8 -*-
import tensorflow as tf

sess = tf.Session()
# 정규분포 따르는 난수로 텐서 생성
print "random_normal 로 정규분포 생성"
t = tf.random_normal([2,3], 3)
tf.initialize_all_variables()
print sess.run(t)

print "셔플해보기 : random_shuffle"
print sess.run(tf.random_shuffle(t))