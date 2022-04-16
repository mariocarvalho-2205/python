'''salario = float(input('Digite o seu Salario R$ '))
aumento = 0.15
novosalario = salario+(salario*aumento)'''
salario = float(input('Digite seu salario R$ '))
novosal = salario + (salario * 15 / 100)


print('Seu salario de R$ {:.2f}, teve {:.0f}% de aumento, e passara a ser de R$ {}{:.2f}{}.'.format(salario, 15, '\033[32m', novosal, '\033[m'))
