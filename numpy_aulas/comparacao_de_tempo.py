from time import time
import numpy as np

# Sem Numpy
# =========
inicio_1 = time()
lista_1 = list(range(10**6))
soma_1 = 0

for i in lista_1:
    soma_1 += i

fim_1 = time()
tempo_1 = fim_1 - inicio_1
print("Sem Numpy")
print(soma_1)
print(tempo_1)


# Com Numpy
# =========
inicio_2 = time()

arr = np.array(lista_1, dtype=float)
soma_2 = arr.sum()

fim_2 = time()
tempo_2 = fim_2 - inicio_2
print("Com Numpy")
print(soma_2)
print(tempo_2)

porcentagem = tempo_2 / tempo_1
print(f"O Numpy executou {porcentagem}% mais rápido")
