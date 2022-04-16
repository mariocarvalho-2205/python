num = int(input('\033[1;32mDigite um numero:\033[m '))
ant = num - 1
suc = num + 1

print('O \033[1;31mantecessor\033[m de \033[1;32m{}\033[m é \033[1;35m{}\033[m'.format(num, ant))
print('O \033[1;33msucessor\033[m de \033[1;32m{}\033[m é \033[1;35m{}\033[m'.format(num, suc))




# Para não quebrar a linha usa o , end=''
# Para centralizar uma string ou inteiro {:^quantidade de espaços}
# Para lateralizar usa os sinais de maior e menor (<esquerda >direita)
# Quebrar a linha usa \n
# Raiz quadrada == num ** (1/2)
# Raiz cubica == num ** (1/3)
# Potencia usando a função interna de potencia pow(numerador, potencia ex: 4,3cubo)
# A função de potencia interna, não segue a ordem de precedencia.