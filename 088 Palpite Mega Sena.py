'''
088 - Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerador e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadastrando em uma lista composta.
'''
import time
from random import randint
from time import sleep
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
print('-=' * 3, f'sorteando {jogos} jogos!'.upper(), '-=' * 3)
for j in range(len(palipte)):
    print(f'Jogo {j + 1}: {palipte[j]}')
    time.sleep(0.8)
print('-=' * 4, f'{"< boa sorte! >":^3}'.upper(), '-=' * 4)




