import pygame
#song = '020 Reproduzir mp3.mp3'
pygame.init()

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

