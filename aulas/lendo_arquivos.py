'''
Quantos municípios em SP
PIB de SP
'''


file_path = "../PIB_100_maiores_cidades_2017.txt"

with open(file_path) as f:
    f_data = f.readlines()

lista_colunas = f_data[0].split(',')
# print(lista_colunas)

linhas = []

for i in range(len(f_data)):
    linhas.append(f_data[i].split(','))

# print(linhas)

colunas_dict = {}

for key in linhas[0]:
    colunas_dict[key] = []
    coluna_n = linhas[0].index(key)

    for i in range(1, len(linhas)):
        colunas_dict[key].append((linhas[i][coluna_n]))

# print(colunas_dict)
# print(colunas_dict['Estado'])

lista_estados = colunas_dict['Estado']
numero_municipios_sp = lista_estados.count('SP')
print(numero_municipios_sp)

pib_acm_sp = 0

for i in range(len(colunas_dict['Estado'])):
    if colunas_dict['Estado'][i] == 'SP':
        pib_acm_sp += float(colunas_dict['Participação (%)'][i])

print(pib_acm_sp)
