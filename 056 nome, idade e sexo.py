# Desenvolva um programma que leia o nome, idade e sexo de 4 pessoas
# No final mostre:
# A media de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos.

nomes = []
idades = []
#sexo = []'''

maioridade = 0
menordevinte = 0
homem_mais_velho = 0

for c in range(1, 3):
    nome = str(input('Digite o {} nome: '.format(c)))
    idade = int(input('Digite a {} idade: '.format(c)))
    idades.append(idade)
    sex = str(input('Digite o sexo da {} pessoa (M) masculino ou (F) feminino: '.format(c))).upper()
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
print('\nA media de todas as idades é {:.0f}'.format(media))
print('temos {} mulher(es) com menos de vinte anos e são: {}.'.format(menordevinte, junto))
print('O homem mais velho é {} com {} anos'.format(homem_mais_velho, maioridade))
