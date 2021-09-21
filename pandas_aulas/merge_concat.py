import pandas as pd
import numpy as np

"""
    pandas.concat(objs: Union[Iterable[FrameOrSeries], Mapping[Label, FrameOrSeries]], axis='0', 
    join: str = "'outer'", ignore_index: bool = 'False', keys='None', levels='None', names='None', 
    verify_integrity: bool = 'False', sort: bool = 'False', copy: bool = 'True')

    pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, 
    right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False,validate=None)
"""

dfa = pd.DataFrame(np.arange(15).reshape(5, 3))
dfb = pd.DataFrame((np.arange(9) ** 2).reshape(3, 3))

print(dfa)
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14

print(dfb)
# Resposta
#     0   1   2
# 0   0   1   4
# 1   9  16  25
# 2  36  49  64


print("\n\nConcat\n======\n")

print(pd.concat([dfa, dfb]))
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14
# 0   0   1   4
# 1   9  16  25
# 2  36  49  64

print(pd.concat([dfa, dfb], ignore_index=True))
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14
# 5   0   1   4
# 6   9  16  25
# 7  36  49  64


print(f"\n\nMerge\n=====\n")

df1 = pd.DataFrame({'id': [1, 2, 3], 'cor': ['branco', 'verde', 'preto']})
print(df1)
# Resposta
#    id     cor
# 0   1  branco
# 1   2   verde
# 2   3   preto

df2 = pd.DataFrame({'times': ['time1', 'time2', 'time3', 'time4', 'time5', ], 'id': [1, 1, 2, 3, 2]})
print(df2)
# Resposta
#    times  id
# 0  time1   1
# 1  time2   1
# 2  time3   2
# 3  time4   3
# 4  time5   2

print(pd.merge(df1, df2))
# Resposta
#    id     cor  times
# 0   1  branco  time1
# 1   1  branco  time2
# 2   2   verde  time3
# 3   2   verde  time5
# 4   3   preto  time4

df3 = pd.DataFrame({'id': [1, 2, 3], 'cor': ['branco', 'verde', 'preto']})
df4 = pd.DataFrame({'times': ['time1', 'time2', 'time3', 'time4', 'time5', ], 'id_cor': [1, 1, 2, 3, 2]})
# Como o id e id_cor são os mesmos tipos de dados com nomes diferentes, usamos left_on e right_on
print(pd.merge(df3, df4, left_on='id', right_on='id_cor'))
# Resposta
#    id     cor  times  id_cor
# 0   1  branco  time1       1
# 1   1  branco  time2       1
# 2   2   verde  time3       2
# 3   2   verde  time5       2
# 4   3   preto  time4       3
