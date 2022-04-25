# 058 Melhore o jogo do DESAFIO 028, onde o computador vai "pensar"
# em um numero entre 0 e 10. Só que agora o jogador vai tentar até
# advinhar até acertar, mostrando no final quantos palpites
# foram necessarios.

# from random import randint -> Aqui importamos apenas a função necessaria.
import random
import time
# computador = randint(0, 10) -> # Dessa forma usamos a função abreviada
                                 # com a importação especifica.
computador = random.randint(0, 10)
print('-_-' * 20)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10. ')
print('Será que você consegue advinhar?')
print('-_-' * 20)
acertou = False # A variavel recebe valor booleano negativo
palpite = 0
while not acertou: # Aqui o laço verifica se booleano é verdadeiro e repete enquanto for falso.
    jogador = int(input('Em que numero eu pensei? '))
    print('Hummm...')
    palpite += 1
    time.sleep(0.5)
    if jogador == computador:
        acertou = True # Se a condição entre jogador e computador for verdadeira,
                       # A variavel acertou, recebe booleano verdadeiro e encerra o laço.
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} palpites.'.format(palpite))


'''tentativas = 0
jogador = 0

while jogador != computador:
    jogador = int(input('Em que numero eu pensei? '))
    tentativas += 1
    print('Processando!!!')
    time.sleep(0.5)
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
    elif jogador == computador:
        print('Parabes!! Você tentou \033[32m{}\033[m vezes até acertar. '.format(tentativas))
        print('O numero que eu escolhi foi o \033[32m{}\033[m e voçê o \033[32m{}\033[m'.format(computador, jogador))
    else:
        print('Que pena, você escolheu \033[31m{}\033[m, e eu escolhi \033[31m{}\033[m'.format(jogador, computador))
        print('Tente de novo!!')'''