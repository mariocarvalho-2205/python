# 071 - Crie um programa que simule o funcionamento
# de um caixa eletronico.
# No inicio pergunte ao usuario qual será o valor sacado
# (numero inteiro) e o programa vai informar quantas cedulas de cada
# valor serão entregues.
# OBS: Considere que o programa possui
# cedulas de R$ 50, R$ 20, R$ 10 e R$ 1

print('=' * 30)
print(f'{"BANCO CARVALHO":^30}')
print('=' * 30)
valor = int(input('Quanto você quer sacar? R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'total de {totalcedula} cedulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break

