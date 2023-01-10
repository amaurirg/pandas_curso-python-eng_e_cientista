import pandas as pd
import openpyxl
from copy import copy

file_path = "preparando_arquivo/rel_sla_teste.xlsx"


text_file = pd.read_excel(file_path, 0) #, header=None)
df = pd.DataFrame(text_file)




linha_titulos = df[df['Unnamed: 0'] == 'O.S.'].index[0]
ini_nacional = df[df['Unnamed: 0'] == 'Nacional'].index[0] + 1
# ini_nacional = linha_titulos
ini_internacional = df[df['Unnamed: 0'] == 'Internacional'].index[0] + 1

linha_nula = df.iloc[ini_internacional-1].isna().all()

df_nacional = df.iloc[ini_nacional:ini_internacional-1]
df_nacional.dropna(axis=0, how='all')
print(df_nacional)

df_internacional = df.iloc[ini_internacional:]
df_internacional.dropna(axis=0, how='all')
#
print(linha_titulos)
print(ini_nacional)
print(ini_internacional)

# # TODO cria coluna
df_nacional['Destino'] = 'NACIONAL'
print(df)
#
# # TODO deleta linha
# # print(df.dropna(axis=0, how='all'))

df.to_excel(file_path, index=False, header=False)
