"""
Alguns métodos para DataFrames

Métodos aplicados ao DataFrame

.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
Deleta linha (axis=0) ou coluna (axis=1) com célula(s) nula(s)

.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
Substitui o valor nulo por um valor determinado

OBS: ESSES MÉTODOS NÃO ALTERAM O OBJETO
"""

import numpy as np
import pandas as pd


a_arr = np.arange(20).reshape(4, 5)
# print(a_arr)
# Resposta
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

b_arr = np.vstack([a_arr, np.array([np.nan, np.nan, np.nan, np.nan, np.nan])])
# print(b_arr)
# Resposta
# [[ 0.  1.  2.  3.  4.]
#  [ 5.  6.  7.  8.  9.]
#  [10. 11. 12. 13. 14.]
#  [15. 16. 17. 18. 19.]
#  [nan nan nan nan nan]]

df_columns = ['A', 'B', 'C', 'D', 'E']
c_df = pd.DataFrame(b_arr, columns=df_columns)
# print(c_df)
# Resposta
#       A     B     C     D     E
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0
# 4   NaN   NaN   NaN   NaN   NaN

# print(c_df.dropna())
# Resposta
#       A     B     C     D     E
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

c_arr = np.vstack([a_arr, np.array([np.nan, np.nan, np.nan, np.nan, np.nan])])
d_df = pd.DataFrame(c_arr, columns=df_columns)
# print(d_df)
# Resposta
#       A     B     C     D     E
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0
# 4   NaN   NaN   NaN   NaN   NaN

d_arr = np.vstack([a_arr, np.array([1, np.nan, np.nan, np.nan, np.nan])])
e_df = pd.DataFrame(d_arr, columns=df_columns)
# print(e_df)
# Resposta
#       A     B     C     D     E
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0
# 4   1.0   NaN   NaN   NaN   NaN

