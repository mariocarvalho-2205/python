# 064 Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando for digitado o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados,
# e qual foi a soma entre eles (desconsiderando o flag).

num = 0
soma = 0
cont = 0

while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        cont += 1
        soma += num

print('Foram lidos {} numeros, e a soma entre eles é {}.'.format(cont, soma))