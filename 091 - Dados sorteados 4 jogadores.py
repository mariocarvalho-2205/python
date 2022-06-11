'''
091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatorios em um dicionario.
No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o
maior numero no dado.
'''
from random import randint
jogadores = dict()
jogadores2 = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6)}
for c in range(0, 4):
    jogadores[f'jogador {c + 1}'] = randint(1, 6)
print(jogadores)
print(jogadores2)