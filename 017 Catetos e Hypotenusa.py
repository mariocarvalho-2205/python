import math #1 importando toda a biblioteca
from math import hypot  # Importando apenas a fum
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) #1 importando toda a biblioteca #2 formula matematica - (co ** 2 + ca ** 2) ** (1/2)
hi2 = hypot(co, ca)  # Importando apenas a função
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'verde':'\033[32m', 'vermelho':'\033[31m'}
print('A hipotenusa vai medir: {}{:.2f}{} '.format(cores['verde'], hi, cores['limpa']))
print('A hipotenusa vai medir: {:.2f} '.format(hi2))
