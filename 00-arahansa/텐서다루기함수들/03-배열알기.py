# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

input = np.array([1, 2, 3])

sess = tf.Session()
tensor = tf.convert_to_tensor(input, dtype=tf.float64)
print tensor

input2 = np.array([[1, 2, 3], [2,4,6]])
tensor2 = tf.convert_to_tensor(input2, dtype=tf.float64)
print tensor2

input3 = np.array([
    [[1,2,3,4], [2,4,6,8], [7,8,9,10]],
    [[11,12,13,8], [12,14,16,8], [1,2,3,4]]
])
tensor3 = tf.convert_to_tensor(input3, dtype=tf.float64)
print tensor3

