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
                           # desejada nome_lista.insert(posição_escolhida, 'item')
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