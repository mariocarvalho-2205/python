n1 = float(input('Digite 1 numero flutuante: '))

# usando função interna int() do python
print('outra forma de converter {} em {} inteiro'.format(n1, int(n1)))

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'verde':'\033[32m', 'vermelho':'\033[31m'}

from math import trunc
num = float(input('Digite o 2 numero flutuante: '))
print('o numero inteiro de {} é {}{}{}'.format(num, cores['azul'], trunc(num), cores['limpa']))

import math
num2 = float(input('Digite outro numero flutuante: '))
print('A porção inteira de {} é {}'.format(num2, math.trunc(num2)))
