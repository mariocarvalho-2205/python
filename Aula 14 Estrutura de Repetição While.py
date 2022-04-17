# Aula 14 - Laço de repetição while
# Laço de repetição while, e´usado quando não sabe qual é o final
# Exemplo 01

'''c = 1
while c != 10:
    print(c)
    c += 1
print('Acabou')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? ')).upper()
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            print('Esse numero é par. ')
            par += 1
        else:
            print('Esse numero é impar. ')
            impar += 1
print('Tivemos {} numeros pares e {} numeros impares'.format(par, impar))

print('Encerramos!! ')
