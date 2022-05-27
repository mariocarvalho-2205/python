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
print()
# Correção:
listanum = []
mai = 0
men = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=' * 30)
print(f'Os numeros digitados foram {listanum}')
print(f'O maior numero digitado foi {mai} na posição ', end=' ')

for c, v in enumerate(listanum):
    if v == mai:
        print(f'{c}...', end=' ')
print(f'\nO menor numero digitado foi {men} na posição ', end=' ')
for c, v in enumerate(listanum):
    if v == men:
        print(f'{c}...', end=' ')






