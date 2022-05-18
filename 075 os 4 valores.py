''' 075 Desenvolva umprograma que leia quatro valores pelo teclado e
guarde-os em uma tupla. no final mostre:
A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o valor 3
C - Quais foram os nmeros pares
'''
num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')),)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


