'''
080 - Crie um programa onde o usuario possa digitar cinco valores numericos
e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela
'''

lista = []

for c in range(0, 5): # Cria a lista com laço de repetição
    num = int(input('Digite um valor: ')) # Recebe o item a ser colocado na lista
    if c == 0 or num > lista[-1]: # Aqui verifica o inicio da lista com o inicio do laço
        lista.append(num) # Adiciona o item lido ao final da lista
        print('Adicionado ao final da lista!')
    else:
        pos = 0 # Variavel ede criação da posição que sera
                # #comparada com a posição da lista
        while pos < len(lista): # Laço de verificação da posição com cada item na lista
            if num <= lista[pos]:      # Verifica se o item digitado é menor
                                       # que cada item da lista junto com a posição.
                lista.insert(pos, num) # para ser adicionado antes do maior
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram {lista}')