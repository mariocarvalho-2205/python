'''
094- Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicionario e todos os
dicionarios em uma lista. No final, mostre:
A-) Quantas pessoas foram cadastradas
B-) A media de idade do grupo
C-) Uma lista com todas as mulheres
D-) Uma lista com todas as pessoas com idade acima da media.
'''
dados = dict()
cadastro = list()
while True:
    dados['Nome'] = str(input('Nome: ')).capitalize().strip()
    dados['Sexo'] = str(input('Sexo? [M/F]: ')).upper().strip()
    dados['Idade'] = int(input('Idade? '))
    cont = str(input('Quer continuar? [S/N]: ')).upper().strip()
    cadastro.append(dados)
    dados.clear()
    if cont == 'N':
        break
print(dados)
print(cadastro)