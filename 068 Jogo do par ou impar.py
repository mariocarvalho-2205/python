# 068 - Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
# minha versão pelo que entendi no enunciado.

from random import randint

print('VAMOS JOGAR PAR OU IMPAR?')
print('*' * 20)
computador = randint(1, 10)


cont = 0
# precisa corrigir o laço. Não está dando o looping e a condição esta errada.
# ganha quando o resto da soma do computador com o num_jogador der a opção escolhida
# pelo jogador
while True:
    num_jogador = int(input('diga um valor: '))
    opc_jogador = str(input('Par ou Impar [P/I] ')).upper().strip()[0]
    total = num_jogador + computador
    soma = num_jogador + computador
    #impar = total % 2 == 1
    if num_jogador != computador:
        if total % 2 == 0:
            print(f'Você jogou {num_jogador} e o computador jogou {computador}. total de {soma} Deu par!')
            print('Você perdeu!')
        if total % 2 == 1:
            print(f'Você jogou {num_jogador} e o computador jogou {computador}. total de {soma} Deu Impar!')
            print('Você perdeu!')
        break
    else:
        if total % 2 == 0:
            print(f'Você jogou {num_jogador} e o computador jogou {computador}. total de {soma} Deu par!')
            print('Você Ganhou!')
        if total % 2 == 1:
            print(f'Você jogou {num_jogador} e o computador jogou {computador}. total de {soma} Deu Impar!')
            print('Você Ganhou!')
    print('Vamos jogar novamente...')

# Essa versão esta dando certo
    '''else:
        print(f'Você jogou {num_jogador} e o computador {computador}. Total de {total} Deu par!!')
        print(f'Você jogou {num_jogador} e o computador {computador}. Total de {total} Deu Impar!!')
'''


'''from random imprt choice

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
