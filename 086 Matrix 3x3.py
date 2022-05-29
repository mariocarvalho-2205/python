'''
086 - Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.
'''
matriz = []

for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input('Digite um numero: ')))
    matriz.append(linha)
print(matriz)
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna], end=' ')
    print()