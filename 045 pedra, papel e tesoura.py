#CORRIGIDO
import random
import time
print('+-' * 20)
print('+-' * 4, 'Pedra, Papel e Tesoura', '+-' * 4)
print('{:*^40}'.format(' JOKENPO '))
print('+-' * 20)
itens = ('Pedra', 'Papel', 'Tesoura') # Criação de uma lista com as opções.
#Variavel computador para mais aleatoria.
computador = int(random.randint(0, 2)) # Opção para mais aleatoria iportando biblioteca
print('''Sua opções:
[ 0 ]: Pedra
[ 1 ]: papel
[ 2 ]: Tesoura''')
jogador = int(input('Qual a sua jogada? ')) # VAriavel do jogador
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')

print('+-' * 20)
print('O Computador escolheu {}'.format(itens[computador]))
# .format(itens[computador]) Varre a lista com a opção escolhida pelo computador
print('jogador escolheu {}'.format(itens[jogador]))
# .format(itens[jogador]) Varre a lista com a opção escolhida pelo jogador
print('+-' * 20)

if computador == 0: # Computador jogou PEDRA!
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Opção Invalida!')
elif computador == 1: # Computador jogou PAPEL!
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Opção Invalida!')

elif computador == 2: # Computador jogou TESOURA!
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção Invalida!')

'''if jogador == 2 and computador == 1: # Computador jogou papel
    print('Tesoura. Voce Ganhou!!')
elif jogador == 2 and computador == 0: # Computador jogou pedra
    print('Pedra. Eu Ganhei!!')
elif jogador == 1 and computador == 2: # Computador jogou Tesoura
    print('Tesoura. Eu ganhei!!')
elif jogador == 1 and computador == 0:
    print('Pedra. Você ganhou!!')
elif jogador == 0 and computador == 1:
    print('Papel. Eu ganhei!!')
elif jogador == 0 and computador == 2:
    print('Pedra. Você ganhou!!')
else:
    print('Deu empate. Escolhemos a mesma coisa!!!')

print(computador)'''