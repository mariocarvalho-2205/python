n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O Segundo valor é maior.')
#elif n1 == n2: pode ser usado com elif tambem declarando a condição.
else:
    print('Os dois numeros sao iguais.')

