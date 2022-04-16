print('\033[32m*-\033[m' * 28)
print('\033[35m-\033[m' * 20, '\033[34mBanco Central\033[m', '\033[35m-\033[m' * 20)
print('\033[32m*-\033[m' * 28)

print('Seja bem vindo. Preciso de alguns dados para continuar.')
v_casa = float(input('Qual o valor da casa a ser financiada? R$ '))
salario = float(input('Qual a sua renda mensal? R$ '))
anos = int(input('Em quantos anos você quer financiar? '))
parcela = v_casa / (anos * 12)
minimo = salario * 0.30

if parcela <= minimo:
    print('\033[33mParabens!\033[m Seu financiamento foi aprovado! ', end='')
    print('O valor da parcela ficará por \033[33mR$ {:.2f}\033[m'.format(parcela))
else:
    print(f'\033[31mLamento!\033[m \033[33mO valor da prestação é de {parcela:.2f} e excede os 30% da sua renda.\033[m')
print('')
