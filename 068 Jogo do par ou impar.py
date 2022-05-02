# 068 - Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
# minha versão pelo que entendi no enunciado.

from random import randint
print('*' * 25)
print('VAMOS JOGAR PAR OU IMPAR?')
print('*' * 25)
cont = 0
vitorias = 0
while True:
    num_jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = num_jogador + computador
    cont += 1
    opc_jogador = ' '
    while opc_jogador not in 'PI':
        opc_jogador = str(input('Par ou Impar [P/I] ')).upper().strip()[0]
    print(f'Você jogou \033[32m{num_jogador}\033[m e o computador jogou {computador}. total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if opc_jogador == 'P':
        if total % 2 == 0:
            print('\033[36mVocê Ganhou!\033[m')
            vitorias += 1
        else:
            print(f'\033[31mVocê Perdeu! Eu ganhei com {cont} tentativas.\033[m')
            break
    elif opc_jogador == 'I':
        if total % 2 == 1:
            print('\033[36mVocê Ganhou!\033[m')
            vitorias += 1
        else:
            print(f'\033[31mVocê Perdeu! Eu ganhei com {cont} tentativas.\033[m')
            break
    print('Vamos jogar novamente...')
    print('_-*' * 10)
print('_-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')




'''from random import randint
print('*' * 25)
print('VAMOS JOGAR PAR OU IMPAR?')
print('*' * 25)
computador = randint(1, 10)
cont = 0
vitorias = 0
while True:
    num_jogador = int(input('Diga um valor: '))
    opc_jogador = str(input('Par ou Impar [P/I] ')).upper().strip()[0]
    total = num_jogador + computador
    cont += 1
    if total % 2 == 0 and opc_jogador == 'P':
        print(f'Você jogou \033[32m{num_jogador}\033[m e o computador jogou {computador}. total de {total}, Deu Par!')
        print('\033[36mVocê Ganhou!\033[m')
        vitorias += 1
    elif total % 2 == 1 and opc_jogador == 'I':
        print(f'Você jogou \033[33m{num_jogador}\033[m e o computador jogou {computador}. total de {total}, Deu Impar!')
        print('\033[36mVocê Ganhou!\033[m')
        vitorias += 1
    elif total % 2 == 0 and opc_jogador == 'I':
        print(f'Você jogou \033[34m{num_jogador}\033[m e o computador jogou {computador}. total de {total}, Deu Par!')
        print(f'\033[31mVocê Perdeu! Eu ganhei com {cont} tentativas.\033[m')
        print('')
        break
    elif total % 2 == 1 and opc_jogador == 'P':
        print(f'Você jogou \033[35m{num_jogador}\033[m e o computador jogou {computador}. total de {total}, Deu Impar!')
        print(f'\033[31mVocê Perdeu! Eu ganhei com {cont} tentativa.\033[m')
        break
    print('Vamos jogar novamente...')
    print('_-*' * 10)
print('_-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')'''


'''from random import choice

print('*' * 10)
print('VAMOS JOGAR PAR OU IMPAR ')
print('*' * 10)

lista = ['P', 'I']
computador = choice(lista)

jogador = ''
cont = 0
while cont < 100:
    jogador = str(input('O que você escolha? ')).upper().strip()
    if jogador != computador:
        break
    else:
        cont += 1
    if jogador != computador:
        break
print()
print(f'Você perdeu!!! Eu joguei {computador}. ', end='')
print(f'Você teve {cont} Vitórias consecutivas.')'''
