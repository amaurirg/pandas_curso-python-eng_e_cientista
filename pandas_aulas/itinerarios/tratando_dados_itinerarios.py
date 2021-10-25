"""
Dados horários de intinerários, pede-se:

    Encontre e filtre as razões sociais que se repetem duas vezes;
    Encontre quais delas possuem intervalos em menos de uma hora.

https://dados.antt.gov.br/dataset/gerenciamento-de-autorizacoes

Uso do método .isin e da função pd.to_datetime

"""

import pandas as pd


filename = 'horarios.csv'
df = pd.read_csv(filename, sep=';', engine='python')
# print(df.head())
# Resposta
#                  cnpj                     razao_social  ... novembro dezembro
# 0  04.192.453/0001-18  ALFA LUZ VIACAO TRANSPORTE LTDA  ...        x        x
# 1  04.192.453/0001-18  ALFA LUZ VIACAO TRANSPORTE LTDA  ...        x        x
# 2  04.192.453/0001-18  ALFA LUZ VIACAO TRANSPORTE LTDA  ...        x        x
# 3  04.192.453/0001-18  ALFA LUZ VIACAO TRANSPORTE LTDA  ...        x        x
# 4  04.192.453/0001-18  ALFA LUZ VIACAO TRANSPORTE LTDA  ...        x        x
#
# [5 rows x 27 columns]

df['time'] = pd.to_datetime(df['horario'])
# print(df.head())
# Acrescentando a coluna time
# Resposta
#                  cnpj  ...                time
# 0  04.192.453/0001-18  ... 2021-10-11 14:00:00
# 1  04.192.453/0001-18  ... 2021-10-11 07:00:00
# 2  04.192.453/0001-18  ... 2021-10-11 07:30:00
# 3  04.192.453/0001-18  ... 2021-10-11 14:00:00
# 4  04.192.453/0001-18  ... 2021-10-11 06:45:00
#
# [5 rows x 28 columns]

# print(df['horario'][1])
# print(type(df['horario'][1]))
# Resposta
# 07:00
# <class 'str'>

# print(df['time'][1])
# print(type(df['time'][1]))
# Resposta
# 2021-10-11 07:00:00
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

diferenca = df['time'][1] - df['time'][2]
# print(diferenca)
# Resposta
# -1 days +23:30:00

filtro_2 = df['razao_social'].value_counts() == 2
# print(filtro_2)
# Resposta
# OSVALDO MENDES & CIA LTDA. - EMPRESA DOIS IRM�OS                  False
# EMPRESA GONTIJO DE TRANSPORTES LTDA.                              False
# VIA��O CAI�ARA LTDA.                                              False
# CONS�RCIO GUANABARA DE TRANSPORTES                                False
# AUTO VIA��O CATARINENSE LTDA.                                     False
#                                                                   ...
# EXPRESSO SANTA MARTA LTDA.                                         True
# ROTA DO SOL TRANSPORTE E TURISMO LTDA                              True
# IRM�OS NASCIMENTO TURISMO LTDA.                                    True
# EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TURISMO LTDA - EPP     True
# VIA��O PARANAIBA LTDA.                                            False
# Name: razao_social, Length: 208, dtype: bool

# print(filtro_2[filtro_2])
# Resposta
# VIA��O TERES�POLIS E TURISMO LTDA.                                 True
# EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TURISMO LTDA - EPP     True
# VIA��O MINEIROS TRANSPORTE E TURISMO LTDA                          True
# VIA��O LUXOR LTDA - LLC TRANSPORTES                                True
# VIACAO JLS LTDA                                                    True
# TRANSPEN TRANSPORTE COLETIVO E ENCOMENDAS LTDA.                    True
# IVAIR CAETANO DO NASCIMENTO ? ME                                   True
# KAWAGUCHI EVENTOS TRANSPORTE E TURISMO LTDA. (CATEDRAL TURISMO)    True
# EMPRESA TESTE SUPAS                                                True
# ROTA DO SOL TRANSPORTE E TURISMO LTDA                              True
# DANISTUR TRANSPORTE RODOVIARIO LTDA                                True
# EXPRESSO SANTA MARTA LTDA.                                         True
# IRM�OS NASCIMENTO TURISMO LTDA.                                    True
# TPC TRANSPORTES LTDA - ME                                          True
# EXPRESSO METR�POLIS TRANSPORTES E VIAGENS LTDA.                    True
# JS SERVI�OS LOGISTICOS LTDA                                        True
# Name: razao_social, dtype: bool

# print(filtro_2[filtro_2].index)
# Resposta
# Index(['VIACAO JLS LTDA', 'DANISTUR TRANSPORTE RODOVIARIO LTDA',
#        'VIA��O LUXOR LTDA - LLC TRANSPORTES',
#        'IVAIR CAETANO DO NASCIMENTO ? ME',
#        'KAWAGUCHI EVENTOS TRANSPORTE E TURISMO LTDA. (CATEDRAL TURISMO)',
#        'EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TURISMO LTDA - EPP',
#        'JS SERVI�OS LOGISTICOS LTDA', 'VIA��O TERES�POLIS E TURISMO LTDA.',
#        'TRANSPEN TRANSPORTE COLETIVO E ENCOMENDAS LTDA.',
#        'EMPRESA TESTE SUPAS', 'ROTA DO SOL TRANSPORTE E TURISMO LTDA',
#        'VIA��O MINEIROS TRANSPORTE E TURISMO LTDA',
#        'TPC TRANSPORTES LTDA - ME',
#        'EXPRESSO METR�POLIS TRANSPORTES E VIAGENS LTDA.',
#        'EXPRESSO SANTA MARTA LTDA.', 'IRM�OS NASCIMENTO TURISMO LTDA.'],
#       dtype='object')

lista_filtrada = list(filtro_2[filtro_2].index)
# Lista com as razões sociais que se repetem duas vezes
# print(lista_filtrada)
# Resposta
# [
#   'JS SERVI�OS LOGISTICOS LTDA', 'ROTA DO SOL TRANSPORTE E TURISMO LTDA',
#   'TRANSPEN TRANSPORTE COLETIVO E ENCOMENDAS LTDA.',
#   'IVAIR CAETANO DO NASCIMENTO ? ME', 'DANISTUR TRANSPORTE RODOVIARIO LTDA',
#   'VIA��O TERES�POLIS E TURISMO LTDA.', 'EMPRESA TESTE SUPAS',
#   'VIA��O LUXOR LTDA - LLC TRANSPORTES', 'IRM�OS NASCIMENTO TURISMO LTDA.',
#   'EXPRESSO METR�POLIS TRANSPORTES E VIAGENS LTDA.',
#   'KAWAGUCHI EVENTOS TRANSPORTE E TURISMO LTDA. (CATEDRAL TURISMO)',
#   'EXPRESSO SANTA MARTA LTDA.', 'TPC TRANSPORTES LTDA - ME', 'VIACAO JLS LTDA',
#   'EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TURISMO LTDA - EPP',
#   'VIA��O MINEIROS TRANSPORTE E TURISMO LTDA'
# ]

# print(df['razao_social'])
# Pegamos toda a coluna razao_social e criamos uma serie com ela
# Resposta
# 0                          ALFA LUZ VIACAO TRANSPORTE LTDA
# 1                          ALFA LUZ VIACAO TRANSPORTE LTDA
# 2                          ALFA LUZ VIACAO TRANSPORTE LTDA
# 3                          ALFA LUZ VIACAO TRANSPORTE LTDA
# 4                          ALFA LUZ VIACAO TRANSPORTE LTDA
#                                ...
# 11472    VTR TRANSPORTE RODOVIARIO DE PASSAGEIROS LTDA ...
# 11473    VTR TRANSPORTE RODOVIARIO DE PASSAGEIROS LTDA ...
# 11474    VTR TRANSPORTE RODOVIARIO DE PASSAGEIROS LTDA ...
# 11475    VTR TRANSPORTE RODOVIARIO DE PASSAGEIROS LTDA ...
# 11476    VTR TRANSPORTE RODOVIARIO DE PASSAGEIROS LTDA ...
# Name: razao_social, Length: 11477, dtype: object

# print(df['razao_social'].isin(lista_filtrada))
# Retorna o DataFrame com os booleanos
# Resposta
# 0        False
# 1        False
# 2        False
# 3        False
# 4        False
#          ...
# 11472    False
# 11473    False
# 11474    False
# 11475    False
# 11476    False
# Name: razao_social, Length: 11477, dtype: bool

# print(df['razao_social'].isin(lista_filtrada).value_counts())
# Retorna quantidade de true e false
# Resposta
# False    11445
# True        32
# Name: razao_social, dtype: int64

# print(df[df['razao_social'].isin(lista_filtrada)])
# Filtrar o o DataFrame com as razões sociais que aparecem 2 vezes
# Resposta
#                      cnpj  ...                time
# 1792   04.801.028/0001-89  ... 2021-10-11 14:00:00
# 1793   04.801.028/0001-89  ... 2021-10-11 09:30:00
# 2934   76.423.366/0001-35  ... 2021-10-11 13:00:00
# 2935   76.423.366/0001-35  ... 2021-10-11 14:00:00
# 3189   02.840.960/0001-95  ... 2021-10-11 10:30:00
# 3190   02.840.960/0001-95  ... 2021-10-11 17:30:00
# 3809   05.939.969/0001-46  ... 2021-10-11 17:15:00
# 3810   05.939.969/0001-46  ... 2021-10-11 07:00:00
# 3850   01.526.151/0001-40  ... 2021-10-11 10:30:00
# 3851   01.526.151/0001-40  ... 2021-10-11 15:30:00
# 4515   02.909.758/0001-72  ... 2021-10-11 07:00:00
# 4516   02.909.758/0001-72  ... 2021-10-11 07:00:00
# 4517   05.768.137/0001-04  ... 2021-10-11 08:00:00
# 4518   05.768.137/0001-04  ... 2021-10-11 09:00:00
# 4877   10.918.268/0001-60  ... 2021-10-11 06:00:00
# 4878   10.918.268/0001-60  ... 2021-10-11 06:00:00
# 5008   07.620.023/0001-48  ... 2021-10-11 06:00:00
# 5009   07.620.023/0001-48  ... 2021-10-11 12:00:00
# 6934   03.103.551/0001-79  ... 2021-10-11 00:00:00
# 6935   03.103.551/0001-79  ... 2021-10-11 00:00:00
# 7494   01.718.370/0001-21  ... 2021-10-11 05:00:00
# 7495   01.718.370/0001-21  ... 2021-10-11 04:30:00
# 7641   75.156.265/0001-82  ... 2021-10-11 08:30:00
# 7642   75.156.265/0001-82  ... 2021-10-11 08:15:00
# 9866   26.428.813/0001-70  ... 2021-10-11 12:00:00
# 9867   26.428.813/0001-70  ... 2021-10-11 12:00:00
# 9868   26.760.933/0001-70  ... 2021-10-11 22:30:00
# 9869   26.760.933/0001-70  ... 2021-10-11 22:30:00
# 9870   09.574.438/0001-58  ... 2021-10-11 04:50:00
# 9871   09.574.438/0001-58  ... 2021-10-11 10:00:00
# 11277  32.179.061/0001-54  ... 2021-10-11 07:00:00
# 11278  32.179.061/0001-54  ... 2021-10-11 17:00:00
#
# [32 rows x 28 columns]

tabela_filtrada = df[df['razao_social'].isin(lista_filtrada)]
# print(tabela_filtrada)
# Resposta
#                      cnpj  ...                time
# 1792   04.801.028/0001-89  ... 2021-10-12 14:00:00
# 1793   04.801.028/0001-89  ... 2021-10-12 09:30:00
# 2934   76.423.366/0001-35  ... 2021-10-12 13:00:00
# 2935   76.423.366/0001-35  ... 2021-10-12 14:00:00
# 3189   02.840.960/0001-95  ... 2021-10-12 10:30:00
# 3190   02.840.960/0001-95  ... 2021-10-12 17:30:00
# 3809   05.939.969/0001-46  ... 2021-10-12 17:15:00
# 3810   05.939.969/0001-46  ... 2021-10-12 07:00:00
# 3850   01.526.151/0001-40  ... 2021-10-12 10:30:00
# 3851   01.526.151/0001-40  ... 2021-10-12 15:30:00
# 4515   02.909.758/0001-72  ... 2021-10-12 07:00:00
# 4516   02.909.758/0001-72  ... 2021-10-12 07:00:00
# 4517   05.768.137/0001-04  ... 2021-10-12 08:00:00
# 4518   05.768.137/0001-04  ... 2021-10-12 09:00:00
# 4877   10.918.268/0001-60  ... 2021-10-12 06:00:00
# 4878   10.918.268/0001-60  ... 2021-10-12 06:00:00
# 5008   07.620.023/0001-48  ... 2021-10-12 06:00:00
# 5009   07.620.023/0001-48  ... 2021-10-12 12:00:00
# 6934   03.103.551/0001-79  ... 2021-10-12 00:00:00
# 6935   03.103.551/0001-79  ... 2021-10-12 00:00:00
# 7494   01.718.370/0001-21  ... 2021-10-12 05:00:00
# 7495   01.718.370/0001-21  ... 2021-10-12 04:30:00
# 7641   75.156.265/0001-82  ... 2021-10-12 08:30:00
# 7642   75.156.265/0001-82  ... 2021-10-12 08:15:00
# 9866   26.428.813/0001-70  ... 2021-10-12 12:00:00
# 9867   26.428.813/0001-70  ... 2021-10-12 12:00:00
# 9868   26.760.933/0001-70  ... 2021-10-12 22:30:00
# 9869   26.760.933/0001-70  ... 2021-10-12 22:30:00
# 9870   09.574.438/0001-58  ... 2021-10-12 04:50:00
# 9871   09.574.438/0001-58  ... 2021-10-12 10:00:00
# 11277  32.179.061/0001-54  ... 2021-10-12 07:00:00
# 11278  32.179.061/0001-54  ... 2021-10-12 17:00:00
#
# [32 rows x 28 columns]

# Criamos duas tabelas dinâmicas pegando o maior e menor time
serie_max = pd.pivot_table(tabela_filtrada, index='razao_social', values=['time'], aggfunc='max')
serie_min = pd.pivot_table(tabela_filtrada, index='razao_social', values=['time'], aggfunc='min')

# print(serie_max)
# Resposta
#                                                                   time
# razao_social
# DANISTUR TRANSPORTE RODOVIARIO LTDA                2021-10-12 14:00:00
# EMPRESA TESTE SUPAS                                2021-10-12 14:00:00
# EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TUR... 2021-10-12 17:30:00
# EXPRESSO METR�POLIS TRANSPORTES E VIAGENS LTDA.    2021-10-12 17:15:00
# EXPRESSO SANTA MARTA LTDA.                         2021-10-12 15:30:00
# IRM�OS NASCIMENTO TURISMO LTDA.                    2021-10-12 07:00:00
# IVAIR CAETANO DO NASCIMENTO ? ME                   2021-10-12 09:00:00
# JS SERVI�OS LOGISTICOS LTDA                        2021-10-12 06:00:00
# KAWAGUCHI EVENTOS TRANSPORTE E TURISMO LTDA. (C... 2021-10-12 12:00:00
# ROTA DO SOL TRANSPORTE E TURISMO LTDA              2021-10-12 00:00:00
# TPC TRANSPORTES LTDA - ME                          2021-10-12 05:00:00
# TRANSPEN TRANSPORTE COLETIVO E ENCOMENDAS LTDA.    2021-10-12 08:30:00
# VIACAO JLS LTDA                                    2021-10-12 12:00:00
# VIA��O LUXOR LTDA - LLC TRANSPORTES                2021-10-12 22:30:00
# VIA��O MINEIROS TRANSPORTE E TURISMO LTDA          2021-10-12 10:00:00
# VIA��O TERES�POLIS E TURISMO LTDA.                 2021-10-12 17:00:00

# print(serie_min)
# Resposta
#                                                                   time
# razao_social
# DANISTUR TRANSPORTE RODOVIARIO LTDA                2021-10-12 09:30:00
# EMPRESA TESTE SUPAS                                2021-10-12 13:00:00
# EXPRESSO BRASILEIRO TRANSPORTE RODOVIARIO E TUR... 2021-10-12 10:30:00
# EXPRESSO METR�POLIS TRANSPORTES E VIAGENS LTDA.    2021-10-12 07:00:00
# EXPRESSO SANTA MARTA LTDA.                         2021-10-12 10:30:00
# IRM�OS NASCIMENTO TURISMO LTDA.                    2021-10-12 07:00:00
# IVAIR CAETANO DO NASCIMENTO ? ME                   2021-10-12 08:00:00
# JS SERVI�OS LOGISTICOS LTDA                        2021-10-12 06:00:00
# KAWAGUCHI EVENTOS TRANSPORTE E TURISMO LTDA. (C... 2021-10-12 06:00:00
# ROTA DO SOL TRANSPORTE E TURISMO LTDA              2021-10-12 00:00:00
# TPC TRANSPORTES LTDA - ME                          2021-10-12 04:30:00
# TRANSPEN TRANSPORTE COLETIVO E ENCOMENDAS LTDA.    2021-10-12 08:15:00
# VIACAO JLS LTDA                                    2021-10-12 12:00:00
# VIA��O LUXOR LTDA - LLC TRANSPORTES                2021-10-12 22:30:00
# VIA��O MINEIROS TRANSPORTE E TURISMO LTDA          2021-10-12 04:50:00
# VIA��O TERES�POLIS E TURISMO LTDA.                 2021-10-12 07:00:00

print(serie_max - serie_min)