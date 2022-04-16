km = int(input('Digite qual a distancia da sua viagem em km: '))

preco = km * 0.50 if km <= 200 else km * 0.45 # usando variavel para condição

if km <= 200:
    #preco = distancia * 0.50
    print('O valor de sua passagem será de R$ {:.2f}'.format(km * 0.50))
else:
    #preco = distancia * 0.45
    print('O valor de sua passagem será de R$ {:.2f}'.format(km * 0.45))

#usando a condição no proprio print
print(f'O valor de sua passagem será de {km * 0.50:.2f}' if km <= 200 else f'O valor de sua passagem será de {km * 0.45:.2f}')


print('Sua passagem será R$ {:.2f}'.format(preco))
