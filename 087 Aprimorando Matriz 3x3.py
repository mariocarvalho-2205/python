'''
087 - Aprimore o desafio anterior, mostrando no final:
A-) A soma de todos os valores pares digitados.
B-) A soma dos valores da terceira coluna.
C-) O maior valor da segunda linha.
'''
# Correção
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
spares = maior = totcoluna = 0
coluna3 = []
for l in range(0 , 3):
    for c in range(0, 3):
        matriz2[l][c] = (int(input(f'Digite um numero para a posição [{l}, {c}]: ')))
        if matriz2[l][c] % 2 == 0:
            pares.append(matriz2[l][c])
print('-=' * 15)
for linha in range(0, len(matriz2)):
    for coluna in range(0, len(matriz2)):
        print(f'{matriz2[linha][coluna]:>3}', end=' ')
        if matriz2[linha][coluna] % 2 == 0:
            spares += matriz2[linha][coluna]
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {spares}')
for linha in range(0, len(matriz2)):
    totcoluna += matriz2[linha][2]
print(f'A soma dos valores da terceira coluna é {totcoluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz2[1][coluna]
    elif matriz2[1][coluna] > maior:
        maior = matriz2[1][coluna]
print(f'O maior valor da segunda linha é {maior}')



# Minha solução
matriz = []
pares = []
coluna3 = []
for l in range(0 , 3):
    lista = []
    for c in range(0, 3):
        num = (int(input(f'Digite um numero para a posição [{l}, {c}]: ')))
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
    matriz.append(lista)
print('-=' * 15)
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz)):
        print(f'{matriz[linha][coluna]:>3}', end=' ')
    print()
print('-=' * 15)
print(f'A soma dos valores pares é {sum(pares)}') # usando as funçoes do python
for linha in range(0, len(matriz)):
    for coluna in range(2, len(matriz)):
        #print(f'{matriz[linha][coluna]:>3}', end=' ')
        coluna3.append(matriz[linha][coluna])
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}') # usando as funçoes do python
print(f'O maior valor da segunda linha é {max(matriz[1])}') # usando as funçoes do python