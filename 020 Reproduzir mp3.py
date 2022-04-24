import pygame
from pygame import mixer
#song = '020 Reproduzir mp3.mp3'
pygame.init()
mixer.init()
mixer.music.load(nome do arquivo.mp3)
mixer.music.set_volume(0.7)
mixer.music.play()

while True:


'''tela = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('Tocando Musica')
branco = (255, 255, 255)
'''
pygame.mixer.music.load('020 Reproduzir mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''
som = pygame.mixer.Sound('WhereAreTheFathers.mp3')
som.play()
som.set_volume(0.5)

run = true
while run:



'''

