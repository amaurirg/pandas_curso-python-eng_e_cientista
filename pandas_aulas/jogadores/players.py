"""
    A partir dos dados de jogadores da NBA (https://www.kaggle.com/drgilermo/nba-players-stats)
    ou arquivo (datasets_1358_30676_Players.csv), pede-se:
        - Qual a média de altura e de peso dos jogadores?,
        - Crie uma nova coluna com a razão peso/altura.,
        - Qual a maior altura, o maior peso, a menor altura e menor peso?,
        - Qual é o estado onde nasce o maior número de jogadores?,
        - Qual o jogador mais alto?
"""

import pandas as pd

file_csv = 'datasets_1358_30676_Players.csv'

read_csv = pd.read_csv(file_csv)

df = pd.DataFrame(read_csv)
print(df.head())
print(list(df.columns))

# todas as médias
print('todas as médias =', df.mean())

# média de altura
print('média de altura =', df.mean()['height'])

# média de peso
print('média de peso =', df.mean()['weight'])

# nova coluna com a razão peso/altura
razao = df['weight'] / df['height']
df['razao'] = razao
print('razao =', razao)
print('\nIncluindo razao:\n', df.head())

# maior altura
print('maior altura =', df['height'].max())

# menor altura
print('menor altura =', df['height'].min())

# maior peso
print('maior peso =', df['weight'].max())

# menor peso
print('menor peso =', df['weight'].min())

# estado onde nasce o maior número de jogadores
state_num_players = df['birth_state'].value_counts().max()
print('state_num_players =', state_num_players)


# jogador mais alto
maior_altura = df.max()['height']
ordenado = df.sort_values(by='height')
print('mais alto:\n', ordenado.tail(3))
# Resposta
# mais alto:
#        Unnamed: 0            Player  height  ...  birth_city  birth_state     razao
# 1711        1711        Manute Bol   231.0  ...     Gogrial  South Sudan  0.389610
# 2297        2297  Gheorghe Muresan   231.0  ...     Triteni      Romania  0.593074
# 223          223               NaN     NaN  ...         NaN          NaN       NaN

# print(df.iloc[3921])
