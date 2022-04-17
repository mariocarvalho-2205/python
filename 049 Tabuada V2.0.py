# Exercício Python 49: Refaça o DESAFIO 9, mostrando a
# tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
num = int(input('Digite um numero: '))
for c in range(0, 10):
    print('{:2} x {:2} = \033[31m{:2}\033[m'.format(num, c + 1, (num*c)))