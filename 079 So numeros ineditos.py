'''
079 - Crie um programa onde o usuario possa digitar varios valores numericos
e cadastre-os em uma lista. Caso o numero já exista la dentro ele não será
adicionado. No final, serão exibidos todos os valores unicos digitados
em ordem crescente
'''
lista = []
print(f'{"=-"*15}')
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!!')
    else:
        print('Numero duplicado! Não vou adicionar...')
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print(f'{"=-"*15}')
print('Você digitou os valores {}'.format(lista))
