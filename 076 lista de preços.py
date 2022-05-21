''' 076 Crie um programa que tenha uma tupla unica com nomes de
produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''

'''lista_produtos = (['Pao', 0.50], ['Cebola', 1.00],
                  ['Açucar', 4.75], ['Feijão', 7.89], ['Arroz', 6.99])
print('-' * 38)
print('{:x^38}'.format(' MS Mercadinho '))
print('-' * 38)
total = 0
for produto, preço in lista_produtos:
    print(f'{produto:.<30}R$  {preço:3.2f}')
    total += preço
print('-' * 38)
print(f'Total {"R$ ":.>27}{total:.2f}')
print('-' * 38)'''


lista = ('lapis', 1.00, 'caderno', 2.50, 'borracha', 3.00, 'tesoura', 5.00, 'lapiseira', 6.00,
         'caneta', 1.99)
print('-' * 39)
print('{:^39}'.format(' Lista de preços '))
print('-' * 39)
total = 0
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$  {lista[pos]:.2f}')
        total += lista[pos]
print('-' * 39)
print(f'{"Total":.<30} R$ {total:.2f}')