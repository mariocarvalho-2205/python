'''
092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionario, se por acaso a CTPS for diferente de ZERO,
o dicionario recebera tambem o ano de contratação e o salario. Calcule e acrescente,
alem da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).capitalize().strip()
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salario: '))
    anos_trabalhados = 35 - (datetime.now().year - dados['Contratação'])
    dados['Aposentadoria'] = dados['Idade'] + anos_trabalhados
print('-=' * 15)
for k, c in dados.items():
    print(f'{k} tem o valor {c}')





