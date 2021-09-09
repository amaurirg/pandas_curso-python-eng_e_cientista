import numpy as np

my_array = np.arange(8).reshape(2, 4) ** 2
my_array[0][0] = 11
print(my_array)
print(my_array.max())
print(my_array.min())
print(my_array.sum())
print(my_array.mean())
print(my_array.std())
# Resposta
# [[11  1  4  9]
#  [16 25 36 49]]
# 49
# 1
# 151
# 18.875
# 15.599979967935857

print("Com parâmetro axis, retorna o maior (no caso do max) valor de cada linha")
print(my_array.max(axis=1))
# [11 49]

print("argmax retorna o índice do elemento com maior valor")
print(my_array.argmax())
# Reposta
# 7

print("argmin retorna o índice do elemento com menor valor")
print(my_array.argmin())
# Reposta
# 1

print("Retorna um array com a soma acumulada, soma os elementos anteriores")
print(my_array.cumsum())
# Resposta
# [ 11  12  16  25  41  66 102 151]
