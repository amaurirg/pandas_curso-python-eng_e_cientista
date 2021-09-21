import pandas as pd
import numpy as np


lista_a = [11, 22, 33, 44, 55]
lista_b = ['a', 'b', 'c', 'd', 'e']

serie_1 = pd.Series(lista_a)
print(serie_1)
# Resposta
# 0    11
# 1    22
# 2    33
# 3    44
# 4    55
# dtype: int64

print(serie_1.shape)
# Resposta
# (5,)

print(serie_1.ndim)     # qtde dimensões
# Resposta
# 1

print(serie_1.size)
# Resposta
# 5

print(serie_1.cumsum())
# Resposta
# 0     11
# 1     33
# 2     66
# 3    110
# 4    165
# dtype: int64

print(serie_1.mean())
# Resposta
# 33.0

# Escolhendo índice
serie_3 = pd.Series(lista_a, index=lista_b)
print(serie_3)
# Resposta
# a    11
# b    22
# c    33
# d    44
# e    55
# dtype: int64

print(serie_3['b'])
# Resposta
# 22

arr = np.arange(10) ** 2
print(arr)
# Resposta
# [ 0  1  4  9 16 25 36 49 64 81]

serie_4 = pd.Series(arr)
print(serie_4)
# Resposta
# 0     0
# 1     1
# 2     4
# 3     9
# 4    16
# 5    25
# 6    36
# 7    49
# 8    64
# 9    81
# dtype: int64

dic = {'a': 123, 'b': 456, 'c': 789}
serie_5 = pd.Series(dic)
print(serie_5)
# Resposta
# O índice são as chaves do dicionário
# a    123
# b    456
# c    789
# dtype: int64

