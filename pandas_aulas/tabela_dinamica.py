import pandas as pd


"""
    pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, 
    dropna=True, margins_name='All', observed=False)
"""

file_csv = 'Acoes_ficticias.csv'

df = pd.read_csv(file_csv, delimiter=';')
print(df)
# Resposta
#     Papel  preco_compra  Quantidade
# 0   PETR4     92.114785         100
# 1   VVAR3     17.519059         100
# 2   ITSA4     56.375177         200
# 3   ITSA4     62.284332         300
# 4   EMBR3     80.626768         100
# 5   ITSA4     77.354576         300
# 6   PETR4      7.330583         100
# 7   PETR4     37.425152         200
# 8   EMBR3     62.691443         300
# 9   VVAR3     58.069377         100
# 10  VVAR3     18.877459         300
# 11  PETR4     84.616718         100
# 12  PETR4     26.778080         200
# 13  PETR4     12.494286         300
# 14  ITSA4     82.849075         100
# 15  EMBR3     32.090326         300
# 16  PETR4     86.766959         100
# 17  EMBR3     66.707810         200
# 18  VVAR3     31.385241         300

print(df.columns)
# Resposta
# Index(['Papel', 'preco_compra', 'Quantidade'], dtype='object')

print(pd.pivot_table(df, index='Papel'))
# Agrupa por 'Papel' e, nesse momento, a média
# O padrão de pivot_table é retornar a média (aggfunc='mean')
# Reposta
# Papel
# EMBR3  225.000000     60.529087
# ITSA4  225.000000     69.715790
# PETR4  157.142857     49.646652
# VVAR3  200.000000     31.462784

print(pd.pivot_table(df, index='Papel', values='preco_compra'))
# Resposta
# Papel
# EMBR3     60.529087
# ITSA4     69.715790
# PETR4     49.646652
# VVAR3     31.462784

print(pd.pivot_table(df, index='Papel', values='Quantidade', aggfunc='sum'))
# Retorna a soma da quantidade agrupada
#        Quantidade
# Papel
# EMBR3         900
# ITSA4         900
# PETR4        1100
# VVAR3         800

df['valor_total'] = df.preco_compra * df.Quantidade
print(df)
# Cria uma nova coluna multiplicando o valor pela quantidade
# Resposta
#     Papel  preco_compra  Quantidade   valor_total
# 0   PETR4     92.114785         100   9211.478515
# 1   VVAR3     17.519059         100   1751.905894
# 2   ITSA4     56.375177         200  11275.035362
# 3   ITSA4     62.284332         300  18685.299477
# 4   EMBR3     80.626768         100   8062.676817
# 5   ITSA4     77.354576         300  23206.372683
# 6   PETR4      7.330583         100    733.058292
# 7   PETR4     37.425152         200   7485.030408
# 8   EMBR3     62.691443         300  18807.432765
# 9   VVAR3     58.069377         100   5806.937731
# 10  VVAR3     18.877459         300   5663.237736
# 11  PETR4     84.616718         100   8461.671786
# 12  PETR4     26.778080         200   5355.616074
# 13  PETR4     12.494286         300   3748.285710
# 14  ITSA4     82.849075         100   8284.907506
# 15  EMBR3     32.090326         300   9627.097887
# 16  PETR4     86.766959         100   8676.695859
# 17  EMBR3     66.707810         200  13341.561964
# 18  VVAR3     31.385241         300   9415.572348

soma_qtde_valor = pd.pivot_table(df, index='Papel', values='Quantidade', aggfunc='sum')
print(soma_qtde_valor)
# Resposta
#        Quantidade
# Papel
# EMBR3         900
# ITSA4         900
# PETR4        1100
# VVAR3         800

soma_qtde_valor = pd.pivot_table(df, index='Papel', values=['Quantidade', 'valor_total'], aggfunc='sum')
print(soma_qtde_valor)
# Resposta
#        Quantidade   valor_total
# Papel
# EMBR3         900  49838.769433
# ITSA4         900  61451.615028
# PETR4        1100  43671.836644
# VVAR3         800  22637.653709

soma_qtde_valor['pmedio'] = soma_qtde_valor.valor_total / soma_qtde_valor.Quantidade
print(soma_qtde_valor)
# Cria uma nova coluna e retorna o preço médio pago pelas ações
# Resposta
#        Quantidade   valor_total     pmedio
# Papel
# EMBR3         900  49838.769433  55.376410
# ITSA4         900  61451.615028  68.279572
# PETR4        1100  43671.836644  39.701670
# VVAR3         800  22637.653709  28.297067

invertendo_para_colunas = pd.pivot_table(df, columns='Papel', values='Quantidade', aggfunc='sum')
print(invertendo_para_colunas)
# Retorna o Papel como coluna
# Resposta
# Papel       EMBR3  ITSA4  PETR4  VVAR3
# Quantidade    900    900   1100    800
