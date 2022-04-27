# 064 Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando for digitado o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados,
# e qual foi a soma entre eles (desconsiderando o flag).


# Minha solução foi usando o if
num = soma = cont = 0

while num != 999:
    num = int(input('Digite um numero diferente de [999 para encerrar]: '))
    if num != 999:
        cont += 1
        soma += num

print('Foram lidos {} numeros, e a soma entre eles é {}.'.format(cont, soma))

# A correção foi dessa forma.
n = s = c = 0
print('2 Versão. ')
n = int(input('Digite um numero. [999 para encerrar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um numero. [999 para encerrar]: '))
print('Foram lidos {} numeros e a soma entre eles é {}.'.format(c, s))
