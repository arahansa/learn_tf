import tensorflow as tf
sess = tf.Session()
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a,b)
mul = tf.mul(a,b)

with tf.Session() as sess :
    print "Addition with variables : %i" % sess.run(add, feed_dict={a:2, b:3})
    print "Multipication with variables : %i " % sess.run(mul, feed_dict={a:2, b:3})

