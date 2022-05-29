'''
084 - Crie um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A-) Quantas pessoas foram cadastradas.
B-)Uma listagem com as pessoas mais pessadas
C-)Uma listagem com as pessoas mais leves
'''
principal = [] # lista principal
temp = [] # lista temporaria.
          # OBS: NÃO PODE ESQUECER DE APAGAR A LISTA A CADA VOLTA DO LAÇO

maior = menor = 0 # variavel para armazenar o maior e o menor valor
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    # Assim que receber os dados, precisa verificar quem e o maior ou menor
    # Poderá ser usado para notas e as medias!!! tambem para pares ou impares.
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:]) # Copiar na lista principal os dados coletados!!!
    temp.clear() # Não esquecer de limpar a lista temporaria
                 # para nao duplicar os nomes na lista principal
    continuar = str(input('Quer continar? [S/N]: ')).strip().upper()
    if continuar in 'N':
        break
print('-+' * 15)
print(f'Os dados foram {principal}')
print(f'Foram cadastradas {len(principal)} pessoas.')
# Aqui começa a verificação para ver se é maior ou menor!!!
print(f'O maior peso foi {maior}kg. Peso de ', end='')
for p in principal: # Usa o contador para varrer a lista principal.
                    # OBS: SEMPRE USAR A LISTA PRINCIPAL!!!
    if p[1] == maior:
        print(f'{p[0].capitalize()}.', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0].capitalize()}.', end=' ')








print('\nPrograma Finalizado com Sucesso!!!')