# Aula 17 - Listas (parte 1)
'''
Variaveis compostas
# Adicionando itens na lista
lista.append('tesoura') # adiciona item na ultima posição da lista

lista.insert(1, 'celular') # adiciona item na posição
                           # desejada nome_lista.insert(posição_escolhida, 'item')

#Apagando itens na lista
del lista[1]    # Apaga itens na lista na posição desejada
lista.pop(3)    # Apaga itens na lista na posição desejada.
                  Se não escolher a posição, vais ser apagado o ultimo item.
lista.remove('telefone') # Apaga itens na lista pelo conteudo
# Usando o metodo .remove verificando se item existe na lista
if 'mesa' in lista:
    lista.remove('mesa')

# Criando lista com função list usando range
lista2 = list(range(2, 11))
# lista aleatoria
lista3 = [1, 5, 3, 9, 7, 6]
# ordenando lista aleatoria
lista3.sort()
# colocando em ordem reversa
lista3.sort(reverse=True)
'''
lista = ['note', 'carro', 'mesa', 'mouse', 'telefone', 'relogio']

print(lista)
lista.append('tesoura') # adiciona item na ultima posição da lista
print(lista)

lista.insert(1, 'celular') # adiciona item na posição
lista.insert(6, 90)        # desejada nome_lista.insert(posição_escolhida, 'item')
print(lista)

#Apagando itens na lista
del lista[1]    # Apaga itens na lista na posição desejada
lista.pop(3)    # Apaga itens na lista na posição desejada
                #  Se não escolher a posição, vais ser apagado o ultimo item.

lista.remove('telefone') # Apaga itens na lista pelo conteudo

if 'mesa' in lista: # Usando o metodo .remove verificando se item existe na lista
    lista.remove('mesa')
print(lista)

# Criando lista com range
lista2 = list(range(2, 11))
print(lista2)
# lista aleatoria
lista3 = [1, 5, 3, 9, 7, 6]
print(lista3)
# ordenando lista aleatoria
lista3.sort()
print(lista3)
# colocando em ordem reversa
lista3.sort(reverse=True)
print(lista3)
lista_remover = [1, 2, 3, 4, 2, 3, 7 ,8 ,2, 2]
print(f'lista remove {lista_remover}')

while 2 in lista_remover:
    lista_remover.remove(2)
    print(f'lista remove sem numero 2 {lista_remover:}')
else:
    print(f'Acabaram os dois da lista {lista_remover}')
for v in lista_remover:
     print(f'{v}...', end='')

#lista3.append('Tenorio')
#lista3.insert(3, 'adilma')

for c, v in enumerate(lista3):
    print(f'\nNa posição {c} encontrei o valor {v}',end='')
print('\nCheguei ao final da lista')

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
'''
a = [1, 2, 3, 8, 95, 65, 21, 54]
# b = a # Dessa forma será criada uma ligação entre as duas lista
        # Sendo assim, toda alteração feita na segunda lista, afetará a segunda.
b = a[:] # dessa forma, é criada uma copia dos valores da primeira lista,
         # podendo alterar os valores apenas na segunda lista
         # Se não fizer dessa forma, o python faz uma ligação
b[3] = 150
print(f'Lista A tem {a}')
print(f'Lista B tem {b}')