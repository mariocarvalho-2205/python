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
mulheres = list()
soma = media = 0
while True:
    dados.clear()  # É preciso esvaziar o dicionario antes de coletar novos dados.
    dados['Nome'] = str(input('Nome: ')).capitalize().strip()
    while True:  # Criamos um laço infinito para validar o sexo.
        dados['Sexo'] = str(input('Sexo? [M/F]: ')).upper().strip()[0]
        if dados['Sexo'] in 'MF':  # Nessa condicional Validamos o sexo. Caso digite errado
            break
        print('ERRO! Por favor digite apenas M ou F.')
    dados['Idade'] = int(input('Idade? '))
    soma += dados['Idade']  # Ao fazer a leitura da idade, somamos a variavel de soma
    cadastro.append(dados.copy())  # É necessario adicionar os dados a
    # lista no final do laço.
    while True:  # laço infinito criado para validar a continuação do cadastro.
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':  # Nessa condicional Validamos a resp. Caso digite errado
            break
        print('ERRO! Por favor digite S ou N.')
    if resp == 'N':  # Aqui encerramos o cadastro e seguimos para a analise.
        break
print('-=' * 20)
print(f'A-) Ao todo temos {len(cadastro)} pessoas cadastradas')
media = soma / len(cadastro)
print(f'B-) A media de idade do grupo é {media:5.2f}')
print(f'C-) As mulheres cadastradas são', end=' ')
for p in cadastro:  # Variavel p varre a lista em busca da chave['Sexo']
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'D-) Lista das pessoas que estão acima da media: ')
for p in cadastro:  # Variavel p varre a lista em busca da chave['Idade']
    if p['Idade'] >= media:  # Condicional para verificar Idade acima da media.
        print('     ', end='')
        for k, v in p.items():  # Laço para varrer os dados da lista
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

