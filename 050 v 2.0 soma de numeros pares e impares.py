# 050 v2.0 - Soma dos Numeros pares e impares.
soma = 0
cont = 0
somaimpar = 0
contimpar = 0

for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num

    if num % 2 == 1:
        contimpar += 1
        somaimpar += num

print('Tivemos \033[32m{}\033[m numeros pares, e a soma entre eles é \033[33m{}\033[m'.format(cont, soma))
print('Tivemos \033[34m{}\033[m numeros impares, e a soma entre eles é \033[35m{}\033[m'.format(contimpar, somaimpar))

