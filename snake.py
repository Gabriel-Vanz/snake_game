
import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def randomize():
    x = random.randint(0,39)
    y = random.randint(0,39)
    return (x * 10, y * 10)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0)) 

bomb = pygame.image.load("assets/bomba.png")
bomb_size = pygame.transform.scale(bomb, (10,10))
bomb_pos = randomize()

letterfont = pygame.font.Font('freesansbold.ttf', 10)

#ajustar range#
def catchLetter():
    sorteio = random.randrange(1,27)
    if sorteio == 0:
        letterfont_a = letterfont.render("A", True, (255,255,255))
        a_pos = randomize()
        return letterfont_a, a_pos
    elif sorteio == 1:
        fontletter_b = letterfont.render("B", True, (255,255,255))
        b_pos = randomize()
        return fontletter_b, b_pos
    elif sorteio == 2:
        fontletra_c = letterfont.render("C", True, (255,255,255))
        c_pos = randomize()
        return fontletra_c, c_pos
    elif sorteio == 3:
        fontletter_d = letterfont.render("D", True, (255,255,255))
        d_pos = randomize()
        return  fontletter_d, d_pos
    elif sorteio == 4:
        fontletter_e = letterfont.render("E", True, (255,255,255))
        e_pos = randomize()
        return fontletter_e, e_pos
    elif sorteio == 5:
        fontletter_f = letterfont.render("F", True, (255,255,255))
        f_pos = randomize()
        return  fontletter_f, f_pos
    elif sorteio == 6:
        fontletter_g = letterfont.render("G", True, (255,255,255))
        g_pos = randomize()
        return fontletter_g, g_pos
    elif sorteio == 7:
        fontletter_h = letterfont.render("H", True, (255,255,255))
        h_pos = randomize()
        return  fontletter_h, h_pos
    elif sorteio == 8:
        fontletter_i = letterfont.render("I", True, (255,255,255))
        i_pos = randomize()
        return fontletter_i, i_pos
    elif sorteio == 9:
        fontletter_j = letterfont.render("J", True, (255,255,255))
        j_pos = randomize()
        return  fontletter_j, j_pos
    elif sorteio == 10:
        fontletter_k = letterfont.render("K", True, (255,255,255))
        k_pos = randomize()
        return fontletter_k, k_pos
    elif sorteio == 11:
        fontletter_l = letterfont.render("L", True, (255,255,255))
        l_pos = randomize()
        return  fontletter_l, l_pos
    elif sorteio == 12:
        fontletter_m = letterfont.render("M", True, (255,255,255))
        m_pos = randomize()
        return fontletter_m, m_pos
    elif sorteio == 13:
        fontletter_n = letterfont.render("N", True, (255,255,255))
        n_pos = randomize()
        return  fontletter_n, n_pos
    elif sorteio == 14:
        fontletter_o = letterfont.render("O", True, (255,255,255))
        o_pos = randomize()
        return fontletter_o, o_pos
    elif sorteio == 15:
        fontletter_p = letterfont.render("P", True, (255,255,255))
        p_pos = randomize()
        return  fontletter_p, p_pos
    elif sorteio == 16:
        fontletter_q = letterfont.render("Q", True, (255,255,255))
        q_pos = randomize()
        return fontletter_q, q_pos
    elif sorteio == 17:
        fontletter_r = letterfont.render("R", True, (255,255,255))
        r_pos = randomize()
        return  fontletter_r, r_pos
    elif sorteio == 18:
        fontletter_s = letterfont.render("S", True, (255,255,255))
        s_pos = randomize()
        return  fontletter_s, s_pos
    elif sorteio == 19:
        fontletter_t = letterfont.render("T", True, (255,255,255))
        t_pos = randomize()
        return  fontletter_t, t_pos
    elif sorteio == 20:
        fontletter_u = letterfont.render("U", True, (255,255,255))
        u_pos = randomize()
        return fontletter_u, u_pos
    elif sorteio == 21:
        fontletter_v = letterfont.render("V", True, (255,255,255))
        v_pos = randomize()
        return  fontletter_v, v_pos
    elif sorteio == 22:
        fontletter_w = letterfont.render("W", True, (255,255,255))
        w_pos = randomize()
        return fontletter_w, w_pos
    elif sorteio == 23:
        fontletter_x = letterfont.render("X", True, (255,255,255))
        x_pos = randomize()
        return  fontletter_x, x_pos
    elif sorteio == 24:
        fontletter_y = letterfont.render("Y", True, (255,255,255))
        y_pos = randomize()
        return fontletter_y, y_pos
    else:
        fontletter_z = letterfont.render("Z", True, (255,255,255))
        z_pos = randomize()
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
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
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

                
                if collision(snake[0], position):
                    letter,position = catchLetter()
                    bomb_pos = randomize()
                    snake.append((0,0))
                    score = score + 1
                    pygame.display.update()

                if collision(snake[0], bomb_pos):
                    game_over = True
                    break
                    
                # Check if snake collided with boundaries
                if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
                    game_over = True
                    break
                
                # Check if the snake has hit itself
                for i in range(1, len(snake) - 1):
                    if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                        game_over = True
                        break

                if game_over:
                    break
                
                for i in range(len(snake) - 1, 0, -1):
                    snake[i] = (snake[i-1][0], snake[i-1][1])
                    
                # Actually make the snake move.
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
                
                for x in range(0, 600, 10): # Draw vertical lines
                    pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
                for y in range(0, 600, 10): # Draw vertical lines
                    pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
                
                score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
                score_rect = score_font.get_rect()
                score_rect.topleft = (600 - 120, 10)
                screen.blit(score_font, score_rect)
                
                for pos in snake:
                    screen.blit(snake_skin,pos)

                pygame.display.update()
        else:
            press_play_font = pygame.font.Font('freesansbold.ttf', 30)
            press_play_screen = press_play_font.render('Pressione a tecla "Espaço" para iniciar', True, (255, 255, 255))
            press_play_rect = press_play_screen.get_rect()
            press_play_rect.midtop = (600 / 2, 10)
            for x in range(0, 600, 10): # Desenho vertical
                pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
            for y in range(0, 600, 10): # Desenho horizontal
                pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
            screen.blit(press_play_screen, press_play_rect)
            screen.blit(letter,position)
            screen.blit(bomb_size, bomb_pos)
            

            pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
