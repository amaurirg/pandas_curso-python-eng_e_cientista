import pandas as pd


file_csv = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file_csv)
print(df.head())
# Resposta
#    Unnamed: 0           Player  height  ...    born   birth_city  birth_state
# 0           0  Curly Armstrong   180.0  ...  1918.0          NaN          NaN
# 1           1     Cliff Barker   188.0  ...  1921.0     Yorktown      Indiana
# 2           2    Leo Barnhorst   193.0  ...  1924.0          NaN          NaN
# 3           3       Ed Bartels   196.0  ...  1925.0          NaN          NaN
# 4           4      Ralph Beard   178.0  ...  1927.0  Hardinsburg     Kentucky
#
# [5 rows x 8 columns]

print(df.columns)
# Resposta
# Index(['Unnamed: 0', 'Player', 'height', 'weight', 'collage', 'born',
#        'birth_city', 'birth_state'],
#       dtype='object')

print(df['birth_state'].value_counts())
# Resposta
# California                  344
# New York                    290
# Illinois                    209
# Pennsylvania                163
# Ohio                        137
#                            ...
# Islamic Republic of Iran      1
# New Hampshire                 1
# Morocco                       1
# Norway                        1
# South Africa                  1
# Name: birth_state, Length: 128, dtype: int64

from_california = df['birth_state'] == 'California'
print(from_california)
# Resposta
# Name: birth_state, Length: 128, dtype: int64
# 0       False
# 1       False
# 2       False
# 3       False
# 4       False
#         ...
# 3917    False
# 3918    False
# 3919    False
# 3920    False
# 3921    False
# Name: birth_state, Length: 3922, dtype: bool

print(from_california.value_counts())
# Retorna que tem 344 jogadores na California
# Resposta
# False    3578
# True      344
# Name: birth_state, dtype: int64

print(df[from_california])
# Resposta
#       Unnamed: 0           Player  height  ...    born     birth_city  birth_state
# 22            22     Bill Calhoun   190.0  ...  1927.0  San Francisco   California
# 50            50      Bob Feerick   190.0  ...  1920.0  San Francisco   California
# 74            74     Alex Hannum*   201.0  ...  1923.0    Los Angeles   California
# 117          117      John Mandic   193.0  ...  1919.0    Los Angeles   California
# 130          130  Vern Mikkelsen*   201.0  ...  1928.0         Fresno   California
# ...          ...              ...     ...  ...     ...            ...          ...
# 3845        3845  Marquese Chriss   208.0  ...  1997.0     Sacramento   California
# 3861        3861  Jonathan Gibson   188.0  ...  1987.0    West Covina   California
# 3890        3890      David Nwaba   193.0  ...  1993.0    Los Angeles   California
# 3894        3894      Gary Payton   193.0  ...  1968.0        Oakland   California
# 3908        3908    Isaiah Taylor   190.0  ...  1994.0        Hayward   California
#
# [344 rows x 8 columns]

print(df['born'] > 1970)
# Retorna jogadores nascidos depois de 1970
# Resposta
# 0       False
# 1       False
# 2       False
# 3       False
# 4       False
#         ...
# 3917    False
# 3918     True
# 3919     True
# 3920     True
# 3921     True
# Name: born, Length: 3922, dtype: bool
