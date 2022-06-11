'''
090 - Faça um programa que leia nome e media de um aluno,
guardando tambem a situação em um dicionário.
No final, mostre o conteudo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).capitalize().strip()
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 7 > aluno['media'] > 5: # ou elif 5 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
# Correção criada com laço para digitar menos linhas
for k, v in aluno.items():
    print(f'\t{k.capitalize()} é igual a {v}')

print(f'\tNome é igual a {aluno["nome"]}')
print(f'\tMédia é igual a {aluno["media"]}')
print(f'\tSituação é igual a {aluno["situacao"]}')
