'''
078 - Crie uma programa que leia 5 valores e guarde-os
numa lista.
No final, mostre qual foi o maior e o menor valor digitado e
as suas respectivas posições.
'''

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Os numeros digitados foram {lista}')
print(f'O maior numero digitado foi {max(lista)} na posição ', end=' ')

for c, v in enumerate(lista):
    if v == max(lista):
        print(f'{c}...', end=' ')
print(f'\nO menor numero digitado foi {min(lista)} na posição ', end=' ')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'{c}...', end=' ')


