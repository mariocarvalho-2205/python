'''059 crie um programa que leia dois valores e mostre um menu na tela.
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('Digite o 1 valor: '))
num2 = int(input('Digite o 2 valor: '))
opcao = ''
while opcao != '5':
    opcao = str(input('''Escolha o que deseja fazer:
 [] Somar
 [] Multiplicar
 [] Maior
 [] Novos Numeros
 [] Sair do Programa: '''))
