'''
082 - Crie um programa que vai ler varios numeros e e colocar em uma lista.

Depois disso, crie duas listas separadas que vao conter apenas os valores pares
e os valores impares digitados, respectivamente.
Ao final, mostre o conteudo das tres listas separadas.
'''

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continar in 'N':
        break
print(f'A lista completa é {lista}')
for c in range(0, len(lista)): # for c, v in enumerate(lista):
    if lista[c] % 2 == 0:      #    if v % 2 == 0:
        pares.append(lista[c]) #        pares.append(v)
    else:                      #    elif v % 2 == 1:
        impares.append(lista[c])#       impares.append(v)
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
