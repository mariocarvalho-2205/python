# 050 - Soma dos Numeros pares.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num

print('Tivemos \033[32m{}\033[m numeros pares, e a soma entre eles é \033[33m{}\033[m'.format(cont, soma))
