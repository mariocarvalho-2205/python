'''
100- Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior.
'''
from random import randint
from time import sleep


def sorteia(lista):
    print('-=' * 30)
    print(f'Sorteando 5 valores: ', end='', flush=True)
    sleep(0.5)
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f'Pronto!!')


def somapar(par):
    pares = 0
    for c in numeros:
        if c % 2 == 0:
            pares += c
    print(f'Somando os valores pares de {numeros}, temos {pares}')
    print('-=' * 30)


numeros = list()
sorteia(numeros)
somapar(numeros)

