
import pygame, random
from pygame.locals import *
from funcoes import Log, Randomize, Collision

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Vai receber nome e e-mail e salva em arquivo.txt
nome = str(input('Digite o seu nome: ')).upper().strip()
email = str(input('Digite seu e-mail: ')).upper().strip()
Log(nome, email)


pygame.init()

#tela
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#icone game
icon = pygame.image.load('assets/snake_icon_game.png')
pygame.display.set_icon(icon)

#corpo da cobra + cor
snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0)) 

#bombas
bomb = pygame.image.load("assets/bomba.png")
bomb_size = pygame.transform.scale(bomb, (10,10))
bomb_pos = Randomize()

letterfont = pygame.font.Font('freesansbold.ttf', 10)

def catchLetter():
    sorteio = random.randrange(1,27)
    if sorteio == 0:
        letterfont_a = letterfont.render("A", True, (255,255,255))
        a_pos = Randomize()
        return letterfont_a, a_pos
    elif sorteio == 1:
        fontletter_b = letterfont.render("B", True, (255,255,255))
        b_pos = Randomize()
        return fontletter_b, b_pos
    elif sorteio == 2:
        fontletra_c = letterfont.render("C", True, (255,255,255))
        c_pos = Randomize()
        return fontletra_c, c_pos
    elif sorteio == 3:
        fontletter_d = letterfont.render("D", True, (255,255,255))
        d_pos = Randomize()
        return  fontletter_d, d_pos
    elif sorteio == 4:
        fontletter_e = letterfont.render("E", True, (255,255,255))
        e_pos = Randomize()
        return fontletter_e, e_pos
    elif sorteio == 5:
        fontletter_f = letterfont.render("F", True, (255,255,255))
        f_pos = Randomize()
        return  fontletter_f, f_pos
    elif sorteio == 6:
        fontletter_g = letterfont.render("G", True, (255,255,255))
        g_pos = Randomize()
        return fontletter_g, g_pos
    elif sorteio == 7:
        fontletter_h = letterfont.render("H", True, (255,255,255))
        h_pos = Randomize()
        return  fontletter_h, h_pos
    elif sorteio == 8:
        fontletter_i = letterfont.render("I", True, (255,255,255))
        i_pos = Randomize()
        return fontletter_i, i_pos
    elif sorteio == 9:
        fontletter_j = letterfont.render("J", True, (255,255,255))
        j_pos = Randomize()
        return  fontletter_j, j_pos
    elif sorteio == 10:
        fontletter_k = letterfont.render("K", True, (255,255,255))
        k_pos = Randomize()
        return fontletter_k, k_pos
    elif sorteio == 11:
        fontletter_l = letterfont.render("L", True, (255,255,255))
        l_pos = Randomize()
        return  fontletter_l, l_pos
    elif sorteio == 12:
        fontletter_m = letterfont.render("M", True, (255,255,255))
        m_pos = Randomize()
        return fontletter_m, m_pos
    elif sorteio == 13:
        fontletter_n = letterfont.render("N", True, (255,255,255))
        n_pos = Randomize()
        return  fontletter_n, n_pos
    elif sorteio == 14:
        fontletter_o = letterfont.render("O", True, (255,255,255))
        o_pos = Randomize()
        return fontletter_o, o_pos
    elif sorteio == 15:
        fontletter_p = letterfont.render("P", True, (255,255,255))
        p_pos = Randomize()
        return  fontletter_p, p_pos
    elif sorteio == 16:
        fontletter_q = letterfont.render("Q", True, (255,255,255))
        q_pos = Randomize()
        return fontletter_q, q_pos
    elif sorteio == 17:
        fontletter_r = letterfont.render("R", True, (255,255,255))
        r_pos = Randomize()
        return  fontletter_r, r_pos
    elif sorteio == 18:
        fontletter_s = letterfont.render("S", True, (255,255,255))
        s_pos = Randomize()
        return  fontletter_s, s_pos
    elif sorteio == 19:
        fontletter_t = letterfont.render("T", True, (255,255,255))
        t_pos = Randomize()
        return  fontletter_t, t_pos
    elif sorteio == 20:
        fontletter_u = letterfont.render("U", True, (255,255,255))
        u_pos = Randomize()
        return fontletter_u, u_pos
    elif sorteio == 21:
        fontletter_v = letterfont.render("V", True, (255,255,255))
        v_pos = Randomize()
        return  fontletter_v, v_pos
    elif sorteio == 22:
        fontletter_w = letterfont.render("W", True, (255,255,255))
        w_pos = Randomize()
        return fontletter_w, w_pos
    elif sorteio == 23:
        fontletter_x = letterfont.render("X", True, (255,255,255))
        x_pos = Randomize()
        return  fontletter_x, x_pos
    elif sorteio == 24:
        fontletter_y = letterfont.render("Y", True, (255,255,255))
        y_pos = Randomize()
        return fontletter_y, y_pos
    else:
        fontletter_z = letterfont.render("Z", True, (255,255,255))
        z_pos = Randomize()
        return  fontletter_z, z_pos

my_direction = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
letter,position = catchLetter()
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
        


    
    if Collision(snake[0], position):
        snake.append((0,0))
        score = score + 1
        letter,position = catchLetter()
        bomb_pos = Randomize()
        pygame.display.update()

    #endgames
    #cobra - bomba
    if Collision(snake[0], bomb_pos):
        game_over = True
        break
        
    # Cobra - bordas
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    # cobra-cobra
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    # movimentação
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    
    screen.fill((0,0,0))
    
    screen.blit(letter,position)
    screen.blit(bomb_size, bomb_pos)
    
    for x in range(0, 600, 10): # linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # linhas horizontais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Pontuação: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()
       
while True:
    screen.fill((0,0,0))
    pygame.display.update()
    game_over_font = pygame.font.Font('freesansbold.ttf', 30)
    game_over_screen = game_over_font.render('Fim de jogo! letras coletadas: ' + str(score), True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(200)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
