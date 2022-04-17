# 052 Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') # coloca a cor quando a condição for realizada
        tot += 1
    else:
        print('\033[31m', end='') # coloca a cor quando a condição for realizada
    print(' {} '.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))

# fora do laçõ de repetição.
if tot == 2: # Verifica se a variavel tot recebeu mais de 2, se for, não e numero primo.
    print('Ele é numero primo.')
else:
    print('Ele não é numero primo.')





