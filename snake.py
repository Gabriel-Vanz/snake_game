import pygame, random
from pygame.locals import *
from defs import letras

#movimentação cobra
def movimento():  
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

def aleatorio():
    x = random.randint(0,79)
    y = random.randint(0,59)
    return (x * 10, y * 10)



def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

fontletras = pygame.font.Font('freesansbold.ttf', 10)
def letras():
    
    p = fontletras.render("A", True, (255,255,255))
    a_pos = aleatorio()

    a = fontletras.render("A", True, (255,255,255))
    a_pos = aleatorio()
    
    i = fontletras.render("I", True, (255,255,255))
    i_pos = aleatorio()


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

#tela
widght = 800
height = 600
tela = pygame.display.set_mode((widght,height))
icone = pygame.image.load("assets/snake_icon_game.png")
pygame.display.set_caption('Snake Palavras')
pygame.display.set_icon(icone)
fps = pygame.time.Clock()


#cobra
cobra = [(200,200), (210,200), (220,200)]
cobra_corpo = pygame.Surface((10,10))
cobra_corpo.fill((0,255,0))
cobra_cabeca = pygame.Surface((cobra [0]))
cobra_cabeca.fill((0,191,0))

direcao = LEFT

#Livros
letras()


#Bombas
bomba = pygame.image.load("assets/bomba.png")
tamanho_bomba = pygame.transform.scale(bomba, (10,10))
bomba_pos = aleatorio()

pontuacao = 0 


while True:
    fps.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
    
    movimento()
    
    if colisao(cobra[0], letras_pos):
        letras_pos = aleatorio()
        cobra.append((0,0))
        pontuacao = pontuacao + 1
        bomba_pos = aleatorio()

        #preciso que, quando forem 10 pontos, gerar +1 bomba por ponto
          
    
    
    #fins de jogo
    if colisao(cobra[0], bomba_pos):
        break
    #chega na borda
    if cobra[0][0] == 800 or cobra[0][1] == 800 or cobra[0][0] < 0 or cobra[0][1] < 0:
        break

    #encosta em si mesma
    for i in range( 1 , len(cobra) - 1 ):
        if cobra[ 0 ][ 0 ] == cobra[i][ 0 ] and cobra[ 0 ][ 1 ] == cobra[i][ 1 ]:
            pygame.quit()
            exit()

    for i in range(len(cobra) -1, 0 , -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])
    


    tela.fill((0,0,0))
    tela.blit(letras, letras_pos)
    tela.blit(tamanho_bomba, bomba_pos)
    #adicionar score com o icone do livro canto superior tela.blit()
    for pos in cobra:
        tela.blit(cobra_corpo, pos)
    

        
        
    pygame.display.update()

