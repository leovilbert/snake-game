import pygame, random, PySimpleGUI as pg
from pygame.locals import *

# função que gera as maçãs aleatoriamente
def on_grid_random():
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    return (x // 10 * 10, y // 10 * 10)

# função para a colisão (com a maçã)
def collision(c1, c2):
    return ((c1[0] == c2[0]) and (c1[1] == c2[1]))

def collision_in_yourself():
        try:
            for i in range (len(snake)):
                if (snake[0][0] == snake[i+1][0]) and (snake[0][1] == snake[i+1][1]):
                    pg.popup(f'Você perdeu! Pontuação: {score}')
                    pygame.quit()
                i += 1
        except IndexError as ie:
            pass

UP = 0
RIGHT = 1 
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')
icon = pygame.image.load('.vscode/snakeIcon.png')
pygame.display.set_icon(icon)

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((50, 255, 50))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 50, 50))

score = 0
my_direction = LEFT

clock = pygame.time.Clock()

# loop onde o jogo acontece
while True:
    clock.tick(20)
    for event in pygame.event.get():
        
        # reconhecendo as setas e direções
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                my_direction = UP
            if event.key == K_DOWN or event.key == K_s:
                my_direction = DOWN
            if event.key == K_LEFT or event.key == K_a: 
                my_direction = LEFT
            if event.key == K_RIGHT or event.key == K_d:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # movimentação da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((25, 25, 25)) # cor do fundo
    screen.blit(apple, apple_pos) # nascimento da maçã
    
    # colisão consigo mesmo
    collision_in_yourself()

    # sair do jogo
    if event.type == QUIT:
        pygame.quit()
        pg.popup(f'Você saiu! Pontuação: {score}')

    for (x, y) in snake:
        screen.blit(snake_skin, (x, y)) # nascimento da cobra
        if x == 600 or x == 0 or y == 600 or y == 0: # caso encoste nas bordas, perde o jogo
            pg.popup(f'Você perdeu! Pontuação: {score}')
            pygame.quit()

    pygame.display.update()
