'''
091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatorios em um dicionario.
No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o
maior numero no dado.
'''
from random import randint
from time import sleep
jogadores = dict()
print('\033[36m-=\033[m' * 21)
print(f'{"Valores Sorteados":^42}')
print('\033[36m-=\033[m' * 21)
for c in range(0, 4):
    jogadores[f'jogador {c + 1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'\tO {k} tirou {v}')
    sleep(.8)
print('\033[36m-=\033[m' * 21)
print(f'{"Ranking dos Jogadores":^42}')
print('\033[36m-=\033[m' * 21)
for i, c in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f'\tO {i + 1}o lugar foi o {c} com {jogadores[c]}')
    sleep(.8)

# segunda versão com 6 jogadores
from operator import itemgetter  # Pesquisar sobre essa biblioteca
jogadores2 = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6),
              'Jogador 5': randint(1, 6), 'Jogador 6': randint(1, 6)}
ranking = list()
print('\033[36m-=\033[m' * 21)
print(f'{"Valores Sorteados":^42}')
print('\033[36m-=\033[m' * 21)
for k, v in jogadores2.items():
    print(f'\tO {k} tirou {v}')
    sleep(.8)
ranking = sorted(jogadores2.items(), key=itemgetter(1), reverse=True)
print('\033[36m-=\033[m' * 21)
print(f'{"Ranking dos Jogadores":^42}')
print('\033[36m-=\033[m' * 21)

for i, v in enumerate(ranking):
    print(f'\tO {i + 1}o lugar foi o {v[0]} com {v[1]}')
    sleep(.8)

for i, c in enumerate(sorted(jogadores2, key=jogadores2.get, reverse=True)):
    print(f'\tO {i + 1}o lugar foi o {c} com {jogadores2[c]}')
    sleep(.8)

