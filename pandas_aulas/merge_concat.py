import pandas as pd
import  numpy as np


dfa = pd.DataFrame(np.arange(15).reshape(5, 3))
dfb = pd.DataFrame((np.arange(9)**2).reshape(3, 3))

print(dfa)
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14

print(dfb)
# Resposta
#     0   1   2
# 0   0   1   4
# 1   9  16  25
# 2  36  49  64


# Concat
# ======

print(pd.concat([dfa, dfb]))
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14
# 0   0   1   4
# 1   9  16  25
# 2  36  49  64

print(pd.concat([dfa, dfb], ignore_index=True))
# Resposta
#     0   1   2
# 0   0   1   2
# 1   3   4   5
# 2   6   7   8
# 3   9  10  11
# 4  12  13  14
# 5   0   1   4
# 6   9  16  25
# 7  36  49  64

print()
print()

# Merge
# =====


df1 = pd.DataFrame({'id': [1, 2, 3], 'cor': ['branco', 'verde', 'preto']})
print(df1)




