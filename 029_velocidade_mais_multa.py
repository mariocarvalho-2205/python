vel = float(input('Digite a velocidade que usou: '))

#Condição composta

if vel > 80:
    print(f'Voce passou a {vel}km e foi multado.')
    multa = (vel - 80) * 7.00
    print('O valor da multa será de R$ {:.2f}'.format(multa))
print('Boa sorte.')

#Condição simples
print(f'Voce passou a {vel}km e foi multado. \nO valor da multa será de R$ {multa:.2f}' if vel > 80 else f'{vel} Esta dentro do limite.')
print('Até a proxima')
