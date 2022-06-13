'''
094- Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicionario e todos os
dicionarios em uma lista. No final, mostre:
A-) Quantas pessoas foram cadastradas
B-) A media de idade do grupo
C-) Uma lista com todas as mulheres
D-) Uma lista com todas as pessoas com idade acima da media.
'''
cadastro = list()
dados = dict()
while True:
    dados.clear()  # É preciso esvaziar o dicionario antes de coletar novos dados.
    dados['Nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        dados['Sexo'] = str(input('Sexo? [M/F]: ')).upper().strip()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    dados['Idade'] = int(input('Idade? '))
    cadastro.append(dados.copy())  # É necessario adicionar os dados a
    # lista no final do laço.
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite S ou N.')
    if resp == 'N':
        break
print(cadastro)
