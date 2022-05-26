'''
081 - Crie umm programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
A-) Quantos numeros foram digitados
B-) A lista de valores ordenada de forma decrescente.
c-) Se o valor 5 foi digitado e está ou nao na lista.
'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print(f'O numero 5 foi encontrado na posição {lista.index(5)}')
else:
    print('O numero 5 não foi encontrado.')
