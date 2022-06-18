'''093- Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em dicionário, incluindo o total de gols feitos
durante o campeonato.'''
dados = dict()
gols = list()
dados['Nome'] = str(input('Nome: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {i + 1}a partida? ')))
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('-=' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for k, v in enumerate(gols):
    print(f'\t=> Na {k + 1}a partida, fez {v} gols.')
print(f'Fez um total de {dados["Total"]} gols.')

