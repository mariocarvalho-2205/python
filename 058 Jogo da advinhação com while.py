# 058 Melhore o jogo do DESAFIO 028, onde o computador vai "pensar"
# em um numero entre 0 e 10. Só que agora o jogador vai tentar até
# advinhar até acertar, mostrando no final quantos palpites
# foram necessarios.

import random
import time

computador = random.randint(1, 4)
print('-_-' * 20)
print('Vou pensar um um numero entre 0 a 10. Tente advinhar? ')
print('-_-' * 20)

tentativas = 0
jogador = 0

while jogador != computador:
    jogador = int(input('Em que numero eu pensei? '))
    tentativas += 1
    print('Processando!!!')
    time.sleep(0.5)
    if jogador == computador:
        print('Parabes!! Você tentou \033[32m{}\033[m vezes até acertar. '.format(tentativas))
        print('O numero que eu escolhi foi o \033[32m{}\033[m e voçê o \033[32m{}\033[m'.format(computador, jogador))
    else:
        print('Que pena, você escolheu \033[31m{}\033[m, e eu escolhi \033[31m{}\033[m'.format(jogador, computador))
        print('Tente de novo!!')