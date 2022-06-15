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
    dados['Gols'] = gols[:]  # Não pode esquecer de criar copia usando o [:]
    dados['Total'] = sum(gols)
    jogadores.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite S ou N')
    if resp == 'N':
        break
    print('-' * 40)
print('-=' * 25)
#print(f'{"Cod":<4}  {"Nome":<10}   {"Gols":<10}   {"Total":<5}')
print(f'{"Cod":<7} ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:<8}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    print('-' * 50)
    if busca == 999:
        print('\t\t\tFINALIZADO COM SUCESSO!!')
        break
    if busca >= len(jogadores):
        print(f'\tERRO! Não existe jogador com codigo {busca}!')
        print('-' * 50)
    else:
        print(f'\t -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}:')
        print(f'\t\tCom um total de {jogadores[busca]["Total"]} gols. ')
        for k, v in enumerate(jogadores[busca]["Gols"]):
            print(f'\t\tNo jogo {k + 1} ele fez {v} gols.')
        print('-' * 50)
print('\t\t\t\t<< VOLTE SEMPRE >>')


