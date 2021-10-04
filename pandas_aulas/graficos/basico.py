import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_aulas.tabela_dinamica import soma_qtde_valor    # para usar o DataFrame


arr = np.arange(10)
print(arr)
# Resposta
# [0 1 2 3 4 5 6 7 8 9]

serie_1 = pd.Series(arr)
print(serie_1)
# Resposta
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# 6    6
# 7    7
# 8    8
# 9    9
# dtype: int64
# Do lado esquerdo são os índices e do lado direito os valores
# Estrutura unidimensional

# serie_1.plot()
# plt.show()

serie_2 = pd.Series(arr.cumsum())
# serie_2.plot()
# plt.show()

df1 = pd.DataFrame({'a': np.arange(50) ** 2, 'b': np.arange(50) * 3, 'c': np.arange(50) * 5})
print(df1)
# Resposta
#        a    b    c
# 0      0    0    0
# 1      1    3    5
# 2      4    6   10
# 3      9    9   15
# 4     16   12   20
# 5     25   15   25
# 6     36   18   30
# 7     49   21   35
# 8     64   24   40
# 9     81   27   45
# 10   100   30   50
# 11   121   33   55
# 12   144   36   60
# 13   169   39   65
# 14   196   42   70
# 15   225   45   75
# 16   256   48   80
# 17   289   51   85
# 18   324   54   90
# 19   361   57   95
# 20   400   60  100
# 21   441   63  105
# 22   484   66  110
# 23   529   69  115
# 24   576   72  120
# 25   625   75  125
# 26   676   78  130
# 27   729   81  135
# 28   784   84  140
# 29   841   87  145
# 30   900   90  150
# 31   961   93  155
# 32  1024   96  160
# 33  1089   99  165
# 34  1156  102  170
# 35  1225  105  175
# 36  1296  108  180
# 37  1369  111  185
# 38  1444  114  190
# 39  1521  117  195
# 40  1600  120  200
# 41  1681  123  205
# 42  1764  126  210
# 43  1849  129  215
# 44  1936  132  220
# 45  2025  135  225
# 46  2116  138  230
# 47  2209  141  235
# 48  2304  144  240
# 49  2401  147  245

# df1.plot()
# plt.show()

# df1.plot(x='c', y=['a', 'b'])
# plt.show()



# DataFrame soma_qtde_valor importado
print(soma_qtde_valor)
# Resposta
# Papel
# EMBR3         900  49838.769433  55.376410
# ITSA4         900  61451.615028  68.279572
# PETR4        1100  43671.836644  39.701670
# VVAR3         800  22637.653709  28.297067


# GRÁFICO DE BARRAS
# =================
# soma_qtde_valor.plot.bar()
# plt.show()

# soma_qtde_valor.plot.bar(y='Quantidade')
# plt.show()


# GRÁFICO DE PIZZA
# =================
# soma_qtde_valor.plot.pie(subplots=True)
# plt.show()

# soma_qtde_valor.plot.pie(y='Quantidade')
# plt.show()


# GRÁFICO DE PIZZA
# =================

filename = 'datasets_1358_30676_Players.csv'
df2 = pd.read_csv(filename)

# df2.plot.scatter(x='born', y='weight')
# plt.show()

df2.plot.scatter(x='height', y='weight')
plt.show()
