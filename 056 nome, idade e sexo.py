# Desenvolva um programma que leia o nome, idade e sexo de 4 pessoas
# No final mostre:
# A media de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos.

nomes = []
idades = []
#sexo = []

maioridade = 0
menordevinte = 0
homem_mais_velho = 0

for c in range(1, 5):
    print('-' * 5,'{} PESSOA '.format(c), '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idades.append(idade)
    sex = str(input('Sexo [M/F]: ')).upper()
    #sexo.append(sex)
    if idade < 20 and sex == 'F':
        menordevinte += 1
        nomes.append(nome)
    if idade > maioridade and sex == 'M':
        maioridade = idade
        homem_mais_velho = nome

junto = ', '.join(nomes)
media = sum(idades) / len(idades)
'''print(nomes)
print(idades)
print(sexo)'''
print('\nA media de todas as idades é {:.1f}'.format(media))
print('temos {} mulher(es) com menos 20 anos e são: {}.'.format(menordevinte, junto))
print('O homem mais velho é {} com {} anos'.format(homem_mais_velho, maioridade))
