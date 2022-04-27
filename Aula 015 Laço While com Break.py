# Nessa aula, vamos aprender como utilizar a
# instrução break e os loopings infinitos a
# favor das nossas estratégias de código.
# É muito importante saber usar o break no Python, j
# á que em alguns casos precisamos interromper um laço no meio
# do caminho.

# 064 Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando for digitado o valor 999,
# que é a condição de parada. No final, mostre quantos numeros foram digitados,
# e qual foi a soma entre eles (desconsiderando o flag)
# Usando o comando Break.

'''Atualização do Python para f strings.'''
# Exemplo

c = s = 0
while True:
    n = int(input('Digite um numero. [999 encerra o programa]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Voçê digitou {c} numeros e a soma entre eles é {s}.')


