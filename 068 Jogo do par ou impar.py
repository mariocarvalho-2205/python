# 068 - Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

import random

print('*' * 10)
print('Par ou Impar?')
print('Vamos ver se você acerta? ')
print('*' * 10)

lista = ['PAR', 'IMPAR']
computador = random.choice(lista)

jogador = ''
cont = 0
while cont < 100:
    jogador = str(input('O que você escolha? ')).upper().strip()
    if jogador != computador:
        break
    else:
        cont += 1
    if jogador != computador:
        break
print(f'Você perdeu!!! Eu joguei {computador}. ', end='')
print(f'Você teve {cont} Vitórias consecutivas.')
