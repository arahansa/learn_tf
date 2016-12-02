import tensorflow as tf
import functions

a1 = tf.Variable([8, 0.1, 0.001, 0.3, 0.5])
functions.showOperation(tf.argmax(a1, 0))

functions.showOperation(tf.argmin(a1, 0))


# ---------------------------------
print "---------------------------"
a2 = tf.Variable([[0.1, 0.3, 0.5]])
functions.showOperation(tf.argmax(a2, 0))
functions.showOperation(tf.argmax(a2, 1))