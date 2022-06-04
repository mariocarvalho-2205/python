'''
086 - Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.
'''

matriz = [] # foi criada a extrutura da matriz

# Loops para criação da lista e sub-listas.
for i in range(0, 3): # esse laço é respónsavel por fazer o loop da lista maior
    linha = []
    for j in range(0, 3): # esse laço e responsavel por fazer o loop das listas internas
        linha.append(int(input(f'Digite um numero para a posição [{i}, {j}]: ')))
    matriz.append(linha)
print(matriz)

# Loops para a exibição das listas (linhas e colunas) usando o range(len(matriz))
for linha in range(len(matriz)): # Esse laço e responsavel por criar a linha
    for coluna in range(len(matriz)): # Esse laço e responsavel por criar a coluna
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
    print()

# Correção

matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # foi criada a extrutura da matriz
                                            # dessa forma, não precisa criar
                                            # outra lista vazia

# Loops para criação da lista e sub-listas.
for i in range(0, 3): # esse laço é respónsavel por fazer o loop da lista maior
    for j in range(0, 3): # esse laço e responsavel por fazer o loop das listas internas
        matriz2[i][j] = (int(input(f'Digite um numero para a posição [{i}, {j}]: ')))
print(matriz)

# Loops para a exibição das listas (linhas e colunas)
for linha in range(0, 3): # Esse laço e responsavel por criar a linha
    for coluna in range(0, 3): # Esse laço e responsavel por crias a coluna
        print(f'[{matriz2[linha][coluna]:^3}]', end=' ')
    print()