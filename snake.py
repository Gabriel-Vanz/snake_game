import pygame, random
from pygame.locals import *


def movimento():  
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

pygame.init()

widght = 500
height = 500
tela = pygame.display.set_mode((widght,height))
icone = pygame.image.load("assets/snake_icon_game.png")
pygame.display.set_caption('Snake Palavras')
pygame.display.set_icon(icone)
fps = pygame.time.Clock()


#cobra
cobra = [(200,200), (210,200), (220,200)]
cobra_corpo = pygame.Surface((10,10))
cobra_corpo.fill((0,0,0))
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

direcao = LEFT
#letras
letras = pygame.image.load("assets/Letra-A-PNG-1-1024x1024.png")
tamanho_letras = pygame.transform.scale(letras, (10,10))
letras_pos = (random.randint(0,490), random.randint(0,490))

while True:
    fps.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_RIGHT:
                direcao = RIGHT
            if event.key == K_LEFT:
                direcao = LEFT
    movimento()


    


    for i in range(len(cobra) -1, 0 , -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])
    

    tela.fill((255,255,255))
    tela.blit(tamanho_letras, letras_pos)
    for pos in cobra:
        tela.blit(cobra_corpo, pos)
        
        
    pygame.display.update()

