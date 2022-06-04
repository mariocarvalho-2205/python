'''
088 - Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerador e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadastrando em uma lista composta.
'''

from random import randint
from time import sleep
# Correção
palpites = []
lista = list()
print('-' * 50)
print(f'{"Jogos da Mega Sena":^50}'.upper())
print('-' * 50)
quantidade = int(input('Quantos jogos você quer que eu sortei? '))
print('-' * 50)
tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    palpites.append(lista[:])
    lista.clear()
    tot += 1
print(f'{"-" * 15}{" Sorteando "}{quantidade}{" Jogos "}{"-" * 15}')
for c, j in enumerate(palpites):
    print(f'O {c + 1}o. palpite é {j}')
    sleep(0.8)
print('-' * 18, 'Boa Sorte!!', '-' * 18)





# Minha solução
'''
print('-=' * 15)
print(f'{"Joga na mega sena":^30}'.upper())
print('-=' * 15)
palipte = []

jogos = int(input('Quantos jogos você quer que eu sortei? '))
for c in range(0, jogos):
    temp = []
    for j in range(0, 6):
        temp.append(randint(1, 60))
    palipte.append(temp)
    temp.clear()
print('-=' * 3, f'sorteando {jogos} jogos!'.upper(), '-=' * 3)
for j in range(len(palipte)):
    print(f'Jogo {j + 1}: {palipte[j]}')
    time.sleep(0.8)
print('-=' * 4, f'{"< boa sorte! >":^3}'.upper(), '-=' * 4)'''




