'''
Quantos municípios em SP
PIB de SP
'''

import pandas as pd


file_path = "../PIB_100_maiores_cidades_2017.txt"


df = pd.read_csv(file_path, engine='python')
# print(df.head())


contador_estados = df['Estado'].value_counts()
print(contador_estados)

is_sp = df['Estado'] == 'SP'
# print(is_sp)

df_sp = df[is_sp]
print(df_sp.head())

pib_sp = df_sp['Participação (%)'].sum()
print(pib_sp)
