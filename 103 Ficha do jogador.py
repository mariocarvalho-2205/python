'''
103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gols na rodade.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():  # Verifica se é numerico, se for, converte o string em inteiro.
    gols = int(gols)  # A variavel recebe o valor com inteiro
else:
    gols = 0
if nome.strip() == '':  # verifica se a string está vazia, se estiver, retornara desconhecido
    ficha(gol=gols)  # Se for desconhecido, retornara o valor da variavel gol com valor int.
else:
    ficha(nome, gols)
