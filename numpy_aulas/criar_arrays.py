import numpy as np


a_1 = np.zeros(6)
print(a_1)
# Resposta
# [0. 0. 0. 0. 0. 0.]

a_2 = np.ones(6) * 11
print(a_2)
# Resposta
# [11. 11. 11. 11. 11. 11.]

a_3 = np.eye(4)
print(a_3)
# Resposta
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
print(a_3.ndim)
# Resposta
# 2

a_4 = np.arange(0, 5, 0.5)
print(a_4)
print(a_4.size)
# Resposta
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
# 10

a_5 = np.linspace(0, 10, 12)
print(a_5)
# Resposta
# [ 0.          0.90909091  1.81818182  2.72727273  3.63636364  4.54545455
#   5.45454545  6.36363636  7.27272727  8.18181818  9.09090909 10.        ]
print(a_5.size)
# Resposta
# 12

a_6 = np.ones(8)
print("a_6", a_6)
# Resposta
# [1. 1. 1. 1. 1. 1. 1. 1.]

a_6.reshape(2, 4)
print("a_6", a_6)
# Resposta
# [1. 1. 1. 1. 1. 1. 1. 1.]

a_7 = np.ones(8)
print("a_7", a_7)
# Resposta
# [1. 1. 1. 1. 1. 1. 1. 1.]

a_7.resize(2, 4)
print("a_7", a_7)
# Resposta
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# OBS: O resize modifica o array e o reshape não

a_8 = np.ones(8)
a_8.resize(2, 4)
print(a_8)
# Resposta
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

a_9 = np.zeros(8)
a_9.resize(2, 4)
print(a_9)
# Resposta
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print("\nvstack e kstack\n")

a_10 = np.vstack((a_8, a_9))
print(a_10)
# Resposta
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

a_11 = np.hstack((a_8, a_9))
print(a_11)
# Resposta
# [[1. 1. 1. 1. 0. 0. 0. 0.]
#  [1. 1. 1. 1. 0. 0. 0. 0.]]

# Copiando um array
# =================

a = np.arange(6)
b = a
print(a)
print(id(a))
print(b)
print(id(b))
c = a.copy()
print(c)
print(id(c))
# Resposta
# 140553083271664
# [0 1 2 3 4 5]
# 140553083271664
# [0 1 2 3 4 5]
# 140553083271376
