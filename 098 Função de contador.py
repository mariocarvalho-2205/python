'''
098- Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep


def contador(i, f, p):
    if p < 0:  # Essa condicional e para resolver o problema do passo negativo
        p *= -1  # Convertendo o passo em positivo
    if p == 0:  # Aqui corrigi o passo se for igual a zero
        p = 1  # Deixando ele com valor de 1
    print('-=' * 15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            cont += p
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            cont -= p
            sleep(0.5)
        print('FIM!')



contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de contar! ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
print('-=' * 15)
