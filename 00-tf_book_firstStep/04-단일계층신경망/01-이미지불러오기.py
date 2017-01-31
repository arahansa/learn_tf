# -*- coding: utf-8 -*-
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
sess = tf.Session()

# 훈련 레이블 은 mnist.train.labels
# 훈련 이미지 mnist.train.images
images = tf.convert_to_tensor(mnist.train.images)
print images.get_shape()
print images

