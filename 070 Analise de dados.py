# 070 Crie um programa que leia o nome de varios produtos
# O programa devera perguntar se o usuario vai continuar.
# No final, mostre:
# A - Qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$ 1000,00
# C - Qual e o nome de produto mais barato

print(f'{"LOJA SUPER MARIO ":^30}')
total = mais_mil = cont = mais_barato = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        mais_mil +=1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa {mais_barato:.2f}')
