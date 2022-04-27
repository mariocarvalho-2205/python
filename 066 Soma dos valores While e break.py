# 066 Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando for digitado o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados,
# e qual foi a soma entre eles (desconsiderando o flag)
# Usando o comando Break.

c = s = 0
while True:
    n = int(input('Digite um numero. [Para encerrar digite 999]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} numeros, e a soma entre eles é {s}.')