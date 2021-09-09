import numpy as np

a = np.arange(10) ** 2
print(a)
# Resposta
# [ 0  1  4  9 16 25 36 49 64 81]

b = np.arange(20).reshape(4, 5)
print(b)
# Resposta
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]

# Para acessar o elemento 6:
print(b[1, 1])
# Resposta
# 6

# Para acessar os elementos 7, 8, 9:
print(b[1, 2:])
# Resposta
# [7 8 9]

# Para uma submatriz:
print(b[2:, 3:])
# Resposta
# [[13 14]
#  [18 19]]

c = np.arange(40).reshape(2, 4, 5)
print(c)
# Resposta
# [[[ 0  1  2  3  4]
#   [ 5  6  7  8  9]
#   [10 11 12 13 14]
#   [15 16 17 18 19]]
#
#  [[20 21 22 23 24]
#   [25 26 27 28 29]
#   [30 31 32 33 34]
#   [35 36 37 38 39]]]

# Para acessar o elemento 26:
print(c[1, 1, 1])
# Resposta
# 26

# Para acessar o elemento 37:
print(c[1, 3, 2])
# Resposta
# 37

d = b[2:, 3:]
print(d is b)
# Resposta
# False

print(d.base is b)
# Resposta
# False

print(d.base is b.base)
# Resposta
# True
