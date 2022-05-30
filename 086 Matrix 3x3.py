'''
086 - Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.
'''
matriz = []

for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input(f'Digite um numero para a posição [{i}, {j}]: ')))
    matriz.append(linha)
print(matriz)
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(f'[{matriz[linha][coluna]:^3}]', end=' ')
    print()