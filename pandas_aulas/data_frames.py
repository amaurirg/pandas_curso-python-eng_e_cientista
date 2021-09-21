'''
Sintaxe:
DataFrame({'key_1': pd.Series(...), 'key_n': pd.Series(...)})
'''
import numpy as np
import pandas as pd

dic = {'coluna1': np.arange(10) * 5, 'coluna2': np.arange(10) ** 2, 'coluna3': np.ones(10)}
print(dic)
# Resposta
# {
#     'coluna1': array([ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45]),
#     'coluna2': array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81]),
#     'coluna3': array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
# }

df = pd.DataFrame(dic)
print(df)
# Resposta
#    coluna1  coluna2  coluna3
# 0        0        0      1.0
# 1        5        1      1.0
# 2       10        4      1.0
# 3       15        9      1.0
# 4       20       16      1.0
# 5       25       25      1.0
# 6       30       36      1.0
# 7       35       49      1.0
# 8       40       64      1.0
# 9       45       81      1.0

arr = np.arange(15).reshape(5, 3)
print(arr)
# Resposta
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]]

df2 = pd.DataFrame(arr)
print(df2)
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14

file = 'jogadores/datasets_1358_30676_Players.csv'
nba_players = pd.read_csv(file)
print(nba_players)
# Resposta
#       Unnamed: 0             Player  ...      birth_city             birth_state
# 0              0    Curly Armstrong  ...             NaN                     NaN
# 1              1       Cliff Barker  ...        Yorktown                 Indiana
# 2              2      Leo Barnhorst  ...             NaN                     NaN
# 3              3         Ed Bartels  ...             NaN                     NaN
# 4              4        Ralph Beard  ...     Hardinsburg                Kentucky
# ...          ...                ...  ...             ...                     ...
# 3917        3917      Troy Williams  ...        Columbia          South Carolina
# 3918        3918       Kyle Wiltjer  ...        Portland                  Oregon
# 3919        3919  Stephen Zimmerman  ...  Hendersonville               Tennessee
# 3920        3920        Paul Zipser  ...      Heidelberg                 Germany
# 3921        3921        Ivica Zubac  ...          Mostar  Bosnia and Herzegovina
#
# [3922 rows x 8 columns]
