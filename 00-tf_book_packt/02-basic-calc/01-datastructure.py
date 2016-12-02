# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
tensor_id = np.array([1.3, 1, 4.0, 23.99])

# np 안에 보기
print tensor_id
print tensor_id[0]
print tensor_id[2]

# 기본속성 Rank 조회
print "기본 속성 Rank :" , tensor_id.ndim
# 텐서의 차원 - 튜플형식 조회
print "텐서의 차원 : ", tensor_id.shape
# 형상
print "형상 : ", tensor_id.dtype

print "======= 텐서플로 변환 ======="
tf_tensor = tf.convert_to_tensor(tensor_id, dtype=tf.float64)
sess = tf.Session()
print sess.run(tf_tensor)
#print sess.run(tf_tensor[0])
#print sess.run(tf_tensor[2])


