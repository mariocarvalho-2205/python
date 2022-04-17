# Exercício Python 49/3: Refaça o DESAFIO 9, mostrando a
# tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for e escolhendo o operador.

num = int(input('Digite um numero: '))
for c in range(1, 11): # é preciso começar pelo 1 e terminar no 11,
                       # assim fica com o inicio e fim correto.
    print('{:2} x {:2} = \033[31m{:2}\033[m'.format(num, c, (num*c)))
