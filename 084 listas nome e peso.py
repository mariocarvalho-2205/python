'''
084 - Crie um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A-) Quantas pessoas foram cadastradas.
B-)Uma listagem com as pessoas mais pessadas
C-)Uma listagem com as pessoas mais leves
'''
pessoas = list()
totpessoas = maispeso = menospeso = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    continuar = str(input('Quer continar? [S/N]: ')).strip().upper()
    if continuar in 'N':
        break
print('-+' * 15)
print(f'Foram cadastradas {totpessoas} pessoas.')
print(pessoas)
print('Programa Finalizado com Sucesso!!!')