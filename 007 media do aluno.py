nome = input('Digite o nome do aluno: ')

n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
media = (n1+n2)/2
print('A media de {} foi {}'.format(nome, media))
if media > 5:
    print('{}, sua media foi {}, e você foi \033[32mAPROVADO!!!\033[m'.format(nome, media))
else:
    print('Powww {}, sua media foi {} e você não passou!!'.format(nome, media), end=" >>> ")
    print('Tentaremos ano que vem.')
print('Até a proxima!!!')




# Para não quebrar a linha usa o , end=''
# Para centralizar uma string ou inteiro {:^quantidade de espaços}
# Para lateralizar usa os sinais de maior e menor (<esquerda >direita)
# Quebrar a linha usa \n
# Raiz quadrada == num ** (1/2)
# Raiz cubica == num ** (1/3)
# Potencia usando a função interna de potencia pow(numerador, potencia ex: 4,3cubo)
# A função de potencia interna, não segue a ordem de precedencia.