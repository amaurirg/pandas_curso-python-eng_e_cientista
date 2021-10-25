"""
Alguns métodos para DataFrames

Métodos aplicados ao DataFrame

.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
Remove uma série de dados especificada

.isnull(obj)/.notnull(obj)
Cria uma série de booleanos

.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
Deleta linha (axis=0) ou coluna (axis=1) com célula(s) nula(s)

.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
Substitui o valor nulo por um valor determinado

.duplicated(subset=None, keep='first')
Retorna um booleano com valores duplicados

.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
Deleta linhas com valores duplicados. Pode selecionar uma determinada coluna usando subset

OBS: ESSES MÉTODOS NÃO ALTERAM O OBJETO
"""

import numpy as np
import pandas as pd

a_arr = np.arange(20).reshape(4, 5)
# print(a_arr)
# Resposta
#  [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

df_columns = ['A', 'B', 'C', 'D', 'E']
a_df = pd.DataFrame(a_arr, columns=df_columns)
# print(a_df)
# Resposta
#     A   B   C   D   E
# 0   0   1   2   3   4
# 1   5   6   7   8   9
# 2  10  11  12  13  14
# 3  15  16  17  18  19

a_df.drop(index=2)
# print(a_df)
# Resposta
#     A   B   C   D   E
# 0   0   1   2   3   4
# 1   5   6   7   8   9
# 2  10  11  12  13  14
# 3  15  16  17  18  19

b_df = a_df.drop(index=2)
# print(b_df)
# Resposta
#     A   B   C   D   E
# 0   0   1   2   3   4
# 1   5   6   7   8   9
# 3  15  16  17  18  19

c_df = a_df.drop(columns='C')
# print(c_df)
# Resposta
#     A   B   D   E
# 0   0   1   3   4
# 1   5   6   8   9
# 2  10  11  13  14
# 3  15  16  18  19

d_df = a_df.drop(index=2, columns='C')
print(d_df)
# Resposta
#     A   B   D   E
# 0   0   1   3   4
# 1   5   6   8   9
# 3  15  16  18  19

