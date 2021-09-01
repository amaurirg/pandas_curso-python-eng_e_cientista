import numpy as np


a = np.sin(90)
print(a)
print(np.pi)
print(np.inf)
print(np.nan)
print(type(np.inf))
print(type(np.nan))
# Resposta
# 0.8939966636005579
# 3.141592653589793
# inf
# nan
# <class 'float'>
# <class 'float'>

a_1 = np.array([[1, 2, 3]])
a_2 = np.array([[4, 5, 6]])
a_3 = a_1 + a_2
print(a_1)
print(a_2)
print(a_3)
# Resposta
# [[1 2 3]]
# [[4 5 6]]
# [[5 7 9]]

a_1 += 5
print(a_1)
# Resposta
# [[6 7 8]]

a_4 = np.array([[1, 2, 3]])
a_5 = np.array([4, 5, 6])
a_6 = a_4.dot(a_5)
print(a_6)
# Resposta
# [32]

