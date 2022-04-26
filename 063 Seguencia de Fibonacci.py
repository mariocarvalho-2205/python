# 063 Escreva um programa que leia um numero n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequencia de Fibonacci.


termos = int(input('Digite quantos numeros da sequencia você quer vê? '))
f1 = 0 # A var F1 recebe 0 que é o inicio da sequencia de Fibonacci
f2 = 1 # A var F2 recebe 1 que é o valor do segundo termo.
f3 = 0 # A var F3 começa com 0, e receberá a soma das vars F1 e F2,
       # para continuar a sequencia.
i = 1
while i <= termos: # O contador irá repetir a quantidade de termos desejada.
    print('{}'.format(f1), end=' -> ')
    f3 = f1 + f2
    f2 = f1
    f1 = f3
    i += 1
print('Fim!!!')
#print('Sequencia finalizada com {} elementos.'.format(i - 1))
