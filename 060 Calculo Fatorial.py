#060 - Faça um programa que leia um numero qualquer e mostre o seu fatorial
# 5! = 5 · 4 · 3 · 2 · 1= 120

# primeira forma
'''from math import factorial
num = int(input('Digite um numero para calcular o seu Fatorial: '))
f = factorial(num)
print('O fatorail de {} é {}'.format(num, factorial(int(num))))'''

# Segunda forma
'''n = int(input('Digite um numero para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='') # usando condicional dentro de um print.
    f *= c
    c -= 1
print('{}'.format(f))'''
n = int(input('Digite um numero para calcular o Fatorial:'))
c = n
f = 1
laco = n + 1
print('Calculando {}!'.format(n), end=' ')
for i in range(f , laco):

    print(' x ' if i > 1 else '= ', end='')
    print('{}'.format(c), end='')
    f *= c
    c -= 1
print(f' = {f}')