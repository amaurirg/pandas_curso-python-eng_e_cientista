import pandas as pd

x = pd.read_excel(
    '/home/amauri/tour_house/Arquivos/ITMUP/ambev-cc/ABC_MapaCentroCusto_60c21790-4fcc-45cd-b52b-e9f2ded5c01f.xls')

sim = x[x['Ativo'] == 'Sim'][['Codigo', 'Ativo']]
nao = x[x['Ativo'] == 'Não'][['Codigo', 'Ativo']]

# print(sim.to_string())
sim['Codigo'].value_counts()
# sim.to_dict(orient='records', into=dict)
sim_groupby = sim.groupby(['Codigo']).count()
print('Total =', sim_groupby)
