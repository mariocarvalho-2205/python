# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de
# zero a vinte.
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso
tuplenum = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
            'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero entre 0 e 20: '))

while True:
    if num < 0 or num > 20:
        num = int(input('Tente novamente!! Digite um numero entre 0 e 20: '))
    else:
        break
print(f'Você digitou o numero {tuplenum[num]}')

while num < 0 or num > 20:
    num = int(input('Tente novamente!! Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {tuplenum[num]}')

#Correção
'''while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {tuplenum[num]}')'''
