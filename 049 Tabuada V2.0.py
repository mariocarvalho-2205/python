# 049 - Tabuada V 2.0
num = int(input('Digite um numero: '))
for c in range(0, 10):
    print('{:2} x {:2} = \033[31m{:2}\033[m'.format(num, c + 1, (num*c)))