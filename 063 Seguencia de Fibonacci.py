# 063 Escreva um programa que leia um numero n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.


termos = int(input('Digite quantos numeros da sequencia você quer vê? '))
f1 = 0
f2 = 1
prox = 0
i = 1
while i <= termos:
    print('{}'.format(f1), end=' -> ')
    prox = f1 + f2
    f2 = f1
    f1 = prox

    i += 1
print('Fim!!!')
#print('Sequencia finalizada com {} elementos.'.format(i - 1))
