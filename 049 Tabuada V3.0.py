# Exercício Python 49/3: Refaça o DESAFIO 9, mostrando a
# tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for e escolhendo o operador.

num = int(input('Digite um numero: '))
operador = str(input('''Digite o operador desejado.
    (A) - Adição
    (S) - Subtração
    (M) - Multiplicação
    (D) - Divisão
    Digite sua mais: ''')).upper()

for c in range(1, 11): # é preciso começar pelo 1 e terminar no 11,
                       # assim fica com o inicio e fim correto.
    if operador == 'A':
        print('{:2}  + {:2} = \033[31m{:2.0f}\033[m'.format(num, c, num + c))
    if operador == 'S':
        print('{:2}  - {:2} = \033[31m{:2.0f}\033[m'.format(num, c - 1, num - (c - 1)))
    if operador == 'M':
        print('{:2}  * {:2} = \033[31m{:2.0f}\033[m'.format(num, c, num * c))
    if operador == 'D':
        print('{:2}  / {:2} = \033[31m{:2.0f}\033[m'.format(num * c, num, (num*c)/num))

