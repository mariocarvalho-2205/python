'''073 crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a - Apenas os 5 primeiros colocados
b - Os ultimos 4 colocados da tabela.
c - Uma lista com os times em ordem alfabetica
d - Em que posição na tabela está o time da chapecoense.
'''
times = ('Corinthias', 'Atletico-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avai', 'America-MG', 'Palmeiras',
         'Bragantino', 'Internacional', 'Fluminense', 'Goias', 'Cuiaba', 'Athletico-PR', 'Flamengo', 'Juventude',
         'Ceara', 'Atletico-GO', 'Fortaleza')

print('-=' * 30)
print(f'Lista de times do Brasileirão {times}')
print('-=' * 30)
print(f'Os 5 primeiros times são: {times[0: 5]}')
print('-=' * 30)
print(f'Os 4 ultimos times são {times[:-5: -1]}')
print('-=' * 30)
print(f'Times em ordem alfabetica {sorted(times)}')
print(f'O Coritiba está na {times.index("Coritiba") + 1} posição')
