import pandas as pd

x = pd.read_excel('/home/amauri/tour_house/Arquivos/ITMUP/ambev-cc/ABC_MapaCentroCusto_60c21790-4fcc-45cd-b52b-e9f2ded5c01f.xls')

filtro_sim = x['Ativo'] == 'Sim'
df_sim = x[filtro_sim]
sim1 = df_sim[['Codigo', 'Ativo']]

# OU

df_sim = x[x['Ativo'] == 'Sim']
sim2 = df_sim[['Codigo', 'Ativo']]


# OU

sim = x[x['Ativo'] == 'Sim'][['Codigo', 'Ativo']]
nao = x[x['Ativo'] == 'Não'][['Codigo', 'Ativo']]
