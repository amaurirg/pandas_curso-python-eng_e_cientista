import pandas as pd
import numpy as np


lista_a = ['a', 'a', 'b', 'c', 'a', 'd', 'c']
lista_b = list(range(7))
dic = {'string': lista_a, 'numeros': lista_b}
print(lista_a)
print(lista_b)
print(dic)
# Resposta
# ['a', 'a', 'b', 'c', 'a', 'd', 'c']
# [0, 1, 2, 3, 4, 5, 6]
# {'string': ['a', 'a', 'b', 'c', 'a', 'd', 'c'], 'numeros': [0, 1, 2, 3, 4, 5, 6]}

df = pd. DataFrame(dic)
print(df)
# Resposta
#   string  numeros
# 0      a        0
# 1      a        1
# 2      b        2
# 3      c        3
# 4      a        4
# 5      d        5
# 6      c        6


# Propriedades
# ============

print(df.shape)
# Resposta
# (7, 2)

print(df.size)
# Resposta
# 14

print(df.ndim)
# Resposta
# 2

print(df.dtypes)
# Resposta
# string     object
# numeros     int64
# dtype: object

print(df.columns)
# Resposta
# Index(['string', 'numeros'], dtype='object')

print(list(df.columns))
# Resposta
# ['string', 'numeros']

print(df.index)
# Resposta
# RangeIndex(start=0, stop=7, step=1)

print(list(df.index))
# Resposta
# [0, 1, 2, 3, 4, 5, 6]


print(df.values)
# Resposta
# [['a' 0]
#  ['a' 1]
#  ['b' 2]
#  ['c' 3]
#  ['a' 4]
#  ['d' 5]
#  ['c' 6]]

print((df.values).shape)
# Resposta
# (7, 2)

print(type(df.values))
# Resposta
# <class 'numpy.ndarray'>


# Métodos
# =======

df2 = pd.DataFrame({'col1': np.arange(100) ** 2, 'col2': np.arange(100) * 5})
print(df2)
# Resposta
#     col1  col2
# 0      0     0
# 1      1     5
# 2      4    10
# 3      9    15
# 4     16    20
# ..   ...   ...
# 95  9025   475
# 96  9216   480
# 97  9409   485
# 98  9604   490
# 99  9801   495
#
# [100 rows x 2 columns]

print(df2.head())
# Resposta
#    col1  col2
# 0     0     0
# 1     1     5
# 2     4    10
# 3     9    15
# 4    16    20


print(df2.head(10))
# Resposta
# 0     0     0
# 1     1     5
# 2     4    10
# 3     9    15
# 4    16    20
# 5    25    25
# 6    36    30
# 7    49    35
# 8    64    40
# 9    81    45

print(df2.tail())
# Resposta
#     col1  col2
# 95  9025   475
# 96  9216   480
# 97  9409   485
# 98  9604   490
# 99  9801   495

print(df2.tail(20))
# Resposta
#     col1  col2
# 80  6400   400
# 81  6561   405
# 82  6724   410
# 83  6889   415
# 84  7056   420
# 85  7225   425
# 86  7396   430
# 87  7569   435
# 88  7744   440
# 89  7921   445
# 90  8100   450
# 91  8281   455
# 92  8464   460
# 93  8649   465
# 94  8836   470
# 95  9025   475
# 96  9216   480
# 97  9409   485
# 98  9604   490
# 99  9801   495

print(df.mean())
# Resposta
# numeros    3.0
# dtype: float64

print(df.max())
# Resposta
# string     d
# numeros    6
# dtype: object

print(df.min())
# Resposta
# string     a
# numeros    0
# dtype: object

print(df.cumsum())
# Retorna a soma cumulativa
# Resposta
#     string  numeros
# 0        a        0
# 1       aa        1
# 2      aab        3
# 3     aabc        6
# 4    aabca       10
# 5   aabcad       15
# 6  aabcadc       21

print(df.cumsum()['string'])
# Resposta
# 0          a
# 1         aa
# 2        aab
# 3       aabc
# 4      aabca
# 5     aabcad
# 6    aabcadc
# Name: string, dtype: object

print(df['string'].value_counts())
# Retorna a qtde que cada elemento tem na lista
# Resposta
# a    3
# c    2
# b    1
# d    1
# Name: string, dtype: int64

print(df.sort_values(by='string'))
# Ordena de acordo com a coluna escolhida em by
# Resposta
#   string  numeros
# 0      a        0
# 1      a        1
# 4      a        4
# 2      b        2
# 3      c        3
# 6      c        6
# 5      d        5

