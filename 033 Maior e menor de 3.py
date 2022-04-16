print('Digite 3 numeros: ')
n1 = int(input('num 1: '))
n2 = int(input('num 2: '))
n3 = int(input('num 3: '))
if (n1 < n2) and (n1 < n3):
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3
if (n1 > n2) and (n1 > n3):
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3
print(f'O maior numero é {maior}\nO menor numero é {menor}')

# segunda alternativa >>> já atribuindo uma das posições na variavel, assim ja eliminamos um if:
menor2 = n1
if n2 < n1 and n2 < n3:
    menor2 = n2
if n3 < n1 and n3 < n2:
    menor2 = n3
maior2 = n1
if n2 > n3 and n2 > n1:
    maior2 = n2
if n3 > n1 and n3 > n2:
    maior2 = n3

print(f'menor é {menor2}')
print(f'maior é {maior2}')





