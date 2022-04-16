import random
import time #olhar biblioteca time
#from time import sleep
#from random import randit
computador = int(random.randint(0, 5))
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar.....')
print('-=-' * 20)

#jogador = int(input('Advinhe qual numero o computador escolheu entre 0 e 5? '))
jogador = int(input('Em que numero eu pensei: '))
#num = int(randit(0 , 5))
print('Processando...')
time.sleep(3) # Função sleep serve para esperar uma quantidade de segundos.

if jogador == computador:
    print(f'Você escolheu {jogador}, voce acertou!!! computador escolheu {computador}.')
else:
    print('Ganhei!! Que pena, seu numero escolhido foi {} e eu escolhi {}'.format(jogador, computador))
print('Até a proxima!!')

#print('Você venceu!' if jogador == computador else 'O computador venceu!!' )