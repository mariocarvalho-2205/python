times = ('Corinthias', 'Atletico-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avai', 'America-MG', 'Palmeiras',
         'Bragantino', 'Internacional', 'Fluminense', 'Goias', 'Cuiaba', 'Athletico-PR', 'Flamengo', 'Juventude',
         'Ceara', 'Atletico-GO', 'Fortaleza')

'''Metodos para utilizar com as tuplas ()
Sao imutaveis e so é permitido apagar a tupla inteira usando o del(tupla)
As tuplas aceitam diversos tipos de dados diferentes na mesma tupla 
Podem ser somadas(concatenadas) assim como as variaveis

len(tupla) - Conta quantos itens tem na tupla
tupla.count(item da lista) - conta a quantidade de objetos na tupla
sorted(tupla) coloca a tupla em ordem alfabetica e transforma em lista
tupla.index(item da tupla ou inicio, e final do fatiamento) verifica a posição de determinado item da lista, OBS: Ele pega 
    a primeira ocorrencia
'''
# Fatiamento de Strings
print(f'oitava posição {times[7]}\n') # pega a posição do fatiamento
print(f'da posição 1 a 7 {times[0:7]}\n') # pega do inicio a posição indicada do fatiamento
print(f'decrescente {times[::-1]}\n') # pega toda a lista no sentido inverso do fim para o inicio
print(sorted(times)) # coloca em ordem convertendo em lista

# laço de repetição for

#for cont in range(0, len(times)): # usando contador e o range com len para pegar o fatiamento
 #   print(f'O {cont+1} time é {times[cont]}') # pega cada item da lista por vez

# usando contador como variavel e o laço {c} para pegar as posiçoes da tupla
'''cont = 1
for c in times:
    print(f'O {cont} time é {c}')
    cont += 1'''
# usando duas variaveis no laço para pégar o numero do laço e a posição na tupla
for pos, time in enumerate(times):
    print(f' o {pos+1} time é {time}')