sal = float(input('Digite o valor do seu salario R$ '))
if sal >= 1250.00:
    aumento = sal + (sal * 0.10) # formula sal + (sal * 10 / 100)
    print('Voce teve um aumento de 10%, e seu salario de R$ {:.2f} passou a ser R$ {:.2f}'.format(sal, aumento))
else:
    aumento = sal + (sal * 0.15) # formula sal + (sal * 15 / 100)
    print('Voce teve um aumento de 15%, e seu salario de R$ {:.2f}, passou a ser R$ {:.2f}'.format(sal, aumento))
