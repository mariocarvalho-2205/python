'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
podemos coletar os dados separando em variaveis
alunos = [n1, n2, n3, n4] = criamos uma lista e atribuimos a ela as variaveis com os dados coletados
'''


import random
#from random import shuffle
alunos = []
cont = 1
qtd = int(input('\033[31mQuantos alunos serão sorteados?\033[m '))
while cont <= qtd:
    nomes = input('\033[36mDigite o nome dos alunos:\033[m ')
    alunos.append(nomes) #append adiciona nomes a uma lista
    cont += 1
print('O aluno escolhido para apagar o quadro foi \033[36m{}\033[m'.format(random.choice(alunos)))
# random.choice(alunos) - Escolhe aleatorio uma opção dentro de uma lista
print(alunos)
random.shuffle(alunos) # embaralha os dados dentro de uma lista mais não exibe

print('A ordem de apresentação dos trabalhos sera: \033[34m{}\033[m'.format(', '.join(alunos)))
