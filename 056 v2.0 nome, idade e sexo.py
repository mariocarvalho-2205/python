# 056 v2.0 Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-' * 5, '{} PESSOA'.format(p), '-' * 5)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} com menos de 20 anos.'.format(totmulher20))