# Aula 18 - Listas (parte 2) / Variaveis Compostas / Matrizes

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(' | ', end='')
        print(matriz[linha][coluna], end=' | ')
    print()

teste = list()
teste.append('Mario') # adiciona itens na ultima posição da lista
teste.append('47')
galera = list() # Criada outra variavel
galera.append(teste[:]) # atribui a variavel o valor da lista anterior.
                        # Usando o [:], cria-se uma copia da liste sem alterar a primeira
                        # sem o [:], quando alteramos a segunda lista, a primeira altera tambem.
teste[0] = 'adilma'
teste[1] = 48
galera.append(teste[:])
print(galera)

galera2 = [['MARIO', 47], ['ADILMA', 48], ['JOAO', 25]]

print(galera2[2][0])

for nome in range(len(galera2)): # Estrutura de repetição para correr linha e coluna
    print()
    for idade in range(len(galera2[nome])):
        print(galera2[nome][idade], end=' ')

for nome in galera2: # Estrutura de repetição para correr linha e coluna
    print(f'{nome[0].capitalize()} tem {nome[1]} de idade.') # Para correr a lista, usa

pessoas = list()                                                             # o contador mais o fatiamento
dado = list()
for c in range(0, 2):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    pessoas.append(dado[:])
    dado.clear()
#print(pessoas)
totmaior = totmenor = 0
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} tem {p[1]} anos, e é maior que 21 anos.')
        totmaior += 1
    else:
        print(f'{p[0]} tem {p[1]} anos, e é menor de 21 anos.')
        totmenor += 1
print(f'Tivemos {totmaior} pessoas maior de idade.'
      f'\nTivemos {totmenor} pessoas menor de idade.')


