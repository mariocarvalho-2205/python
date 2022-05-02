# 069 Crie umprograma que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar
# se o usuario quer ou não continuar.
# No final, mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de vinte anos.

print('-' * 20)
print('Cadastre uma pessoa')
print('-' * 20)
continuar = ''
idade = maior_18 = menos_20 = homens = 0

while True:
    idade = int(input('IDADE: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menos_20 += 1
    print('-' * 20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-' * 20)
    if continuar == 'N':
        break
print('_-' * 20)
print('FIM DO PROGRAMA')
print('_-' * 20)
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {homens} homens cadastrados. ')
print(f'E temos {menos_20} mulheres com menos de 20 anos.')
