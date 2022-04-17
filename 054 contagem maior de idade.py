# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
ano = datetime.date.today().year

from datetime import date
atual = date.today().year
maior = 0
menor = 0

listamaior = [] # usando lista para somar no lugar de variavel.
listamenor = []

for c in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu?  '.format(c)))
    idade = atual - nasc # usando variavel para achar a idade.
    #if (atual - nasc) >= 21:  - sem usar variavel idade.
    if idade >= 21:
        maior += 1
        listamaior.append(nasc)
    else:
        menor += 1
        listamenor.append(nasc)
print('Temos {} pessoas maior de idade, e {} menor de idade'.format(maior, menor))

print('Temos {} pessoas maior de idade, e {} menor de idade'.format(len(listamaior), len(listamenor)))


