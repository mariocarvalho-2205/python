# 056 Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''

for p in range(1, 5):
    print('-' * 5, '{} PESSOA'.format(p), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))