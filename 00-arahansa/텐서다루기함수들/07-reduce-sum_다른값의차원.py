# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

sess = tf.Session()

input1 = np.array([
    [[1,2,3,4]],
    [[11,12,13,8]]
])

input2 = np.array([
    [[3,6,3,4], [2,4,6,8]]
])


tensor1 = tf.convert_to_tensor(input1, dtype=tf.float32)
tensor2 = tf.convert_to_tensor(input2, dtype=tf.float32)
print "tensor1:", tensor1
print "tensor2:", tensor2

print "--- sub ---"
print sess.run(tf.sub(tensor1, tensor2))
print "--- reduce_sum --- "
print sess.run(tf.reduce_sum(tf.sub(tensor1, tensor2)))