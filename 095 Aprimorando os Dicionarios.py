'''
095- Aprimore o Desafio 093 para que ele funcione com varios jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
jogadores = list()
dados = dict()
gols = list()
while True:
    dados.clear()
    gols.clear()  # Corrigir o erro que está repetindo os valores em todas as listas.
    dados['Nome'] = str(input('Nome: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {i + 1}a partida? ')))
        dados['Gols'] = gols
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite S ou N')
    if resp == 'N':
        break

print('-=' * 20)
print(jogadores)
print(f'{"Cod":<4}  {"Nome":<10}   {"Gols":<10}   {"Total":<5}')
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'\t=> Na {k + 1}a partida, fez {v} gols.')
print(f'Fez um total de {dados["Total"]} gols.')