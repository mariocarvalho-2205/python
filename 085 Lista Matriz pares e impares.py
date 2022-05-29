'''
085 - Crie um programa onde o usuario possa digitar 7 valores numericos e
cadastre-os em uma lista unica que mantenha os valores separados pares e impares.
No final, mostre os valores pares e impares em ordem crescente.
'''
numeros = [[],[]]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    if num % 2 == 1:
        numeros[1].append(num)
print(f'Os numeros pares foram {sorted(numeros[0])}')
print(f'Os numeros impares foram {sorted(numeros[1])}')