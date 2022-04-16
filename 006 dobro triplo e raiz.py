print('\033[32m-\033[m\033[33m*\033[m' * 17)
num = int(input('\033[4;31mDigite um numero:\033[m '))
print('-*' * 17)
dob = num * 2
tri = num * 3
raiz = num**(1/2)

print('O \033[4;34mdobro\033[m de {:*<10} é {:*>10}'.format(num, dob))
print('O \033[4;36mtriplo\033[m de {:-^10} é {}'.format(num, tri))
print('A \033[4;31mRaiz\033[m de {} é {:.2f}'.format(num, raiz))
print('A \033[4;33mpotencia\033[m de {} é {}'.format(num, pow(num,3)))





# Para não quebrar a linha usa o , end=''
# Para centralizar uma string ou inteiro {:^quantidade de espaços}
# Para lateralizar usa os sinais de maior e menor (<esquerda >direita)
# Quebrar a linha usa \n
# Raiz quadrada == num ** (1/2)
# Raiz cubica == num ** (1/3)
# Potencia usando a função interna de potencia pow(numerador, potencia ex: 4,3cubo)
# A função de potencia interna, não segue a ordem de precedencia.