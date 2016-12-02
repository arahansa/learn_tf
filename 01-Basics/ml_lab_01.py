# https://github.com/FuZer/Study_TensorFlow/
import tensorflow as tf
hello = tf.constant("hello TensorFlow");
sess = tf.Session()
print sess.run(hello);