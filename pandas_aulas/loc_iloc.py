import pandas as pd


"""
    - loc[i,j], onde i e j são os nomes dos índices
    - iloc[i,j], onde i e j são os números dos índices
"""

file_csv = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file_csv)
print(df.head())

print(df.columns)
# Resposta
# Index(['Unnamed: 0', 'Player', 'height', 'weight', 'collage', 'born',
#        'birth_city', 'birth_state'],
#       dtype='object')

print(df.loc[1:4, ['height', 'birth_state']])
# Pega somente as coluna height e birth_state
# Resposta
#    height birth_state
# 1   188.0     Indiana
# 2   193.0         NaN
# 3   196.0         NaN
# 4   178.0    Kentucky

print(df.loc[1:4, 'height':'birth_state'])
# Pega da coluna height ate a coluna birth_state
# Resposta
#    height  weight  ...   birth_city  birth_state
# 1   188.0    83.0  ...     Yorktown      Indiana
# 2   193.0    86.0  ...          NaN          NaN
# 3   196.0    88.0  ...          NaN          NaN
# 4   178.0    79.0  ...  Hardinsburg     Kentucky
#
# [4 rows x 6 columns]

print(df.loc[1:4:2, 'height':'birth_state'])
# Resposta
# 1   188.0    83.0  ...   Yorktown      Indiana
# 3   196.0    88.0  ...        NaN          NaN
#
# [2 rows x 6 columns]

print(df.loc[1:4, 'height':'birth_state':2])
# Resposta
#    height                          collage   birth_city
# 1   188.0           University of Kentucky     Yorktown
# 2   193.0         University of Notre Dame          NaN
# 3   196.0  North Carolina State University          NaN
# 4   178.0           University of Kentucky  Hardinsburg

print(df.iloc[1:4, ::])
# Resposta
# 1           1   Cliff Barker   188.0  ...  1921.0   Yorktown      Indiana
# 2           2  Leo Barnhorst   193.0  ...  1924.0        NaN          NaN
# 3           3     Ed Bartels   196.0  ...  1925.0        NaN          NaN
#
# [3 rows x 8 columns]

print(df.iloc[1:4, 2:5])
# Pega da coluna 2 a 5 com os índices de 1 a 3 (1:4)
# Resposta
#    height  weight                          collage
# 1   188.0    83.0           University of Kentucky
# 2   193.0    86.0         University of Notre Dame
# 3   196.0    88.0  North Carolina State University



