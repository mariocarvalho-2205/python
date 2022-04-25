'''059 crie um programa que leia dois valores e mostre um menu na tela.
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
num1 = int(input('Digite o 1 valor: '))
num2 = int(input('Digite o 2 valor: '))
opcao = 0

while opcao != 5: # O laço verifica o valor digitado na var-opção.
  # Var-opção recebe valor inserido pelo usuario.
  opcao = int(input('''\nEscolha o que deseja fazer:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do Programa:
Digite sua opção: '''))
  print('Processando....')
  sleep(1)
  if opcao == 1:
    soma = num1 + num2
    print('Opção 1 - O resultado da soma entre {} + {} é {}'.format(num1, num2, soma))
  elif opcao == 2:
    multi = num1 * num2
    print('Opção 2 - A multiplicação enter {} x {} é {}'.format(num1, num2, multi))
  elif opcao == 3:
    if num1 > num2:
      maior = num1
    elif num2 > num1:
      maior = num2
      print('Opção 3. Entre {} e {} o maior numero é {}'.format(num1, num2, maior))
    else:
      print('Os numeros são iguais.')
  elif opcao == 4:
    print('Digite novos numeros: ')
    num1 = int(input('Digite o 1 valor: '))
    num2 = int(input('Digite o 2 valor: '))
  elif opcao == 5:
    print('O programa será finalizado.')
  else:
    print('Digite uma opção valida.')
print('Finalizando....')
sleep(1)
print('Fim do programa. Volte Sempre!!')