'''
087 - Aprimore o desafio anterior, mostrando no final:
A-) A soma de todos os valores pares digitados.
B-) A soma dos valores da terceira coluna.
C-) O maior valor da segunda linha.
'''
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
print(f'A soma dos valores pares é {sum(pares)}')
for linha in range(0, len(matriz)):
    for coluna in range(2, len(matriz)):
        #print(f'{matriz[linha][coluna]:>3}', end=' ')
        coluna3.append(matriz[linha][coluna])
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')