"""
.isnull(obj)/.notnull(obj)
Cria uma série de booleanos

OBS: ESSE MÉTODO NÃO ALTERA O OBJETO
"""

import numpy as np
import pandas as pd


a_arr = np.arange(20).reshape(4, 5)

b_arr = np.vstack([a_arr, np.array([np.nan, np.nan, np.nan, np.nan, np.nan])])
# print(b_arr)
# Resposta
# [[ 0.  1.  2.  3.  4.]
#  [ 5.  6.  7.  8.  9.]
#  [10. 11. 12. 13. 14.]
#  [15. 16. 17. 18. 19.]
#  [nan nan nan nan nan]]

b_df = pd.DataFrame(b_arr)
# print(b_df)
# Resposta
#       0     1     2     3     4
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0
# 4   NaN   NaN   NaN   NaN   NaN

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

# print(c_df.isnull())
# Resposta
#        A      B      C      D      E
# 0  False  False  False  False  False
# 1  False  False  False  False  False
# 2  False  False  False  False  False
# 3  False  False  False  False  False
# 4   True   True   True   True   True

# print(c_df.notnull())
# Resposta
# 0   True   True   True   True   True
# 1   True   True   True   True   True
# 2   True   True   True   True   True
# 3   True   True   True   True   True
# 4  False  False  False  False  False

# print(c_df['A'].notnull())
# Resposta
# 0     True
# 1     True
# 2     True
# 3     True
# 4    False
# Name: A, dtype: bool

print(c_df[c_df['A'].notnull()])
# Resposta
#       A     B     C     D     E
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   6.0   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

print(c_df[c_df['A'].isnull()])
# Resposta
#     A   B   C   D   E
# 4 NaN NaN NaN NaN NaN

