# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

tensor_2d = np.array([(1,2,3,4), (4,5,6,7), (8,9,10,11),(12,13,14,15)])
print tensor_2d

print "3행3형 값 얻기", tensor_2d[3][3]

print "배열의 일부분 접근 : 를 이용함 ==> " , tensor_2d[0:2, 0:2]


matrix1 = np.array([(2,2,2), (2,2,2), (2,2,2)], dtype='int32')
matrix2 = np.array([(1,1,1), (1,1,1), (1,1,1)], dtype='int32')

print "matrix1 = "
print matrix1

print "matrix2 = "
print matrix2

matrix3 = np.array([(2, 7, 2), (1,4,2), (9, 0, 2)], dtype='float32')
print "matrix3 = "
print matrix3
print "===== 이 밑은 텐서플로우 ======"

matrix1 = tf.constant(matrix1)
matrix2 = tf.constant(matrix2)
matrix_product = tf.matmul(matrix1, matrix2)
matrix_sum = tf.add(matrix1, matrix2)
matrix_det = tf.matrix_determinant(matrix3)

sess = tf.Session()
print "matrix1 * mat 2 \n", sess.run(matrix_product)
print "matrix1 + mat 2 \n", sess.run(matrix_sum)
print "mat3 determinant(행렬식) result ", sess.run(matrix_det)



