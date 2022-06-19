'''
099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def maior(* num):
    cont = 0
    print('-=' * 25)
    print('Analisando os valores passados...')
    sleep(0.5)
    while cont <= len(num) - 1:
        print(f'{num[cont]}', end=' ', flush=True)
        cont += 1
        sleep(0.5)
    sleep(0.5)
    print(f'Foram passados {len(num)} numeros ao todo.', flush=True)
    sleep(0.5)
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}.', flush=True)
    else:
        num = 0
        print(f'O maior valor foi {num}.')


maior(2, 9, 4, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


def maior2(* num):
    cont = maior = 0
    print('-=' * 25)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = cont
        else:
            if valor > cont:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior2(2, 9, 4, 7, 1)
maior2(4, 7, 0)
maior2(1, 2)
maior2(6)
maior2()
