''' Usando o Jupyter mostrará a equação simbólica '''

import sympy as sp


c = sp.symbols('c')
# print(c*c)

sp.init_printing()

lista_simbolos = ['y', 'x']
y, x = sp.symbols(lista_simbolos)

f_x_y = x**2 + y**2 + x*y
# print(f_x_y)
# Resposta  𝑥2+𝑥𝑦+𝑦2


resposta = f_x_y.subs(x, 1).subs(y, 2)
# print(resposta)
# Resposta 7

f_xy = (x+y)**2 + y**2 + 2*x*y + y**2
# print(f_xy)
# Resposta 2𝑥𝑦+2𝑦2+(𝑥+𝑦)2
simplificada = sp.simplify(f_xy)
# print(simplificada)
# Resposta 𝑥2+4𝑥𝑦+3𝑦2

# print(x <= y)
# Resposta 𝑥≤𝑦
