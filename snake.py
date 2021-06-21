import pygame, random
from pygame.locals import *


#Movimentação cobra
def movimento():  
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

#Surgimento de bombas e letras aleatorias
def aleatorio():
    x = random.randint(0,39)
    y = random.randint(0,39)
    return (x * 10, y * 10)

#Verificar se cobra encostou na bomba ou nas letras
def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

#tela, ícone, nome
widght = 400
height = 400
tela = pygame.display.set_mode((widght,height))
icone = pygame.image.load("assets/snake_icon_game.png")
pygame.display.set_caption('Snake Palavras')
pygame.display.set_icon(icone)
fps = pygame.time.Clock()


#cobra
cobra = [(200,200), (210,200), (220,200)]
cobra_corpo = pygame.Surface((10,10))
cobra_corpo.fill((0,255,0))

direcao = LEFT

#Letras
fontletras = pygame.font.Font('freesansbold.ttf', 10)
    
fontletra_p = fontletras.render("P", True, (255,255,255))
p_pos = aleatorio()

fontletra_a = fontletras.render("A", True, (255,255,255))
a_pos = aleatorio()
    
fontletra_i = fontletras.render("I", True, (255,255,255))
i_pos = aleatorio()



#Bombas
bomba = pygame.image.load("assets/bomba.png")
tamanho_bomba = pygame.transform.scale(bomba, (10,10))
bomba_pos = aleatorio()

pontuacao = 0 

jogando = True
while jogando:
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




    #se pontuação == 0 , letra P, pontuação +1, 
    #se pontuação == 1, letra A, pontuação +1,
    #se pontuação == 2, letra I, pontuação +1
    if pontuacao == 0:
        tela.fill((0,0,0))
        tela.blit(fontletra_p, p_pos)
        pygame.display.update()
        

    if colisao(cobra[0], p_pos) and pontuacao == 0:
        a_pos = aleatorio()
        tela.blit(fontletra_a, a_pos)
        cobra.append((0,0))
        pontuacao = pontuacao + 1
        bomba_pos = aleatorio()
        pygame.display.update()
        
    elif colisao(cobra[0], a_pos) and pontuacao == 1:
        i_pos = aleatorio()
        tela.blit(fontletra_i, i_pos)
        cobra.append((0,0))
        pontuacao = pontuacao + 1
        bomba_pos = aleatorio() 
        pygame.display.update()

        #a cada letra adicionar +1 bomba
        #ta crescendo desenfreadamente
        
    
    
    #fins de jogo

    #cobra-bomba
    if colisao(cobra[0], bomba_pos):
        jogando = False
        break


    #cobra-borda
    if cobra[0][0] == 400 or cobra[0][1] == 400 or cobra[0][0] < 0 or cobra[0][1] < 0:
        jogando = False 
        break

    #cobra-cobra
    for i in range( 1 , len(cobra) - 1 ):
        if cobra[ 0 ][ 0 ] == cobra[i][ 0 ] and cobra[ 0 ][ 1 ] == cobra[i][ 1 ]:
            jogando = False
            break


    tela.blit(tamanho_bomba, bomba_pos)
    #adicionar as letras coletadas em cima


    for pos in cobra:
        tela.blit(cobra_corpo, pos)
    
    for i in range(len(cobra) -1, 0 , -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    for x in range(0, 400, 10): 
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 400))
    for y in range(0, 400, 10): 
        pygame.draw.line(tela, (40, 40, 40), (0, y), (400, y))
        
        
    pygame.display.update()

while not jogando:
    voce_perdeu = pygame.font.Font('freesansbold.ttf', 30)
    voce_perdeu_tela = voce_perdeu.render("Você Perdeu!" , True, (255,255,255))
    voce_perdeu_ret = voce_perdeu_tela.get_rect()
    voce_perdeu_ret.midtop = (400 / 2, 25)
    tela.blit(voce_perdeu_tela, voce_perdeu_ret)
    pygame.display.update()
    pygame.time.wait(300)
    while not jogando:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jogando = True