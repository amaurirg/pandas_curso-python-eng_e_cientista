import numpy as np


a_1 = np.array([1, 1, 1])
print(a_1)
print(a_1.shape)
print(a_1.ndim)
# Resposta
# [1 1 1]
# (3,)
# 2

a_1 = np.array([[1, 1, 1]])
print(a_1)
print(a_1.shape)
print(a_1.ndim)
# Resposta
# [[1 1 1]]
# (1, 3)
# 1

a_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a_2)
print(a_2.shape)
print(a_2.size)
print(a_2.ndim)
print(a_2.dtype)
# Resposta
# [[1 2 3]
#  [4 5 6]]
# (2, 3)
# 6
# 2
# int64

a_2 = np.array([[1, 2., 3], [4, 5, 6]])
print(a_2)
print(a_2.dtype)
# Resposta
# [[1. 2. 3.]
#  [4. 5. 6.]]
# float64

# OBS: O array só aceita 1 tipo de dado.
# Podemos observar que somente 1 item é float e a resposta dtype foi float
# Abaixo colocamos uma string e todos os itens foram convertidos em string

a_2 = np.array([['python', 2., 3], [4, 5, 6]])
print(a_2)
print(a_2.dtype)
# Resposta
# [['python' '2.0' '3']
#  ['4' '5' '6']]
# <U32

a_3 = np.arange(27).reshape(3, 3, 3)
print(a_3)
# Resposta
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]
