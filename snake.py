import pygame, random, PySimpleGUI
from pygame.locals import *

def main():
    # função que gera as maçãs aleatoriamente
    def on_grid_random():
        x = random.randint(20, 580)
        y = random.randint(20, 580)
        return (x // 20 * 20, y // 20 * 20)

    # função para a colisão (com a maçã)
    def collision(c1, c2):
        return ((c1[0] == c2[0]) and (c1[1] == c2[1]))

    # função para a colisão (consigo mesmo)
    def collision_in_yourself():
        try:
            for i in range (len(snake)):
                if (snake[0][0] == snake[i+1][0]) and (snake[0][1] == snake[i+1][1]):
                    PySimpleGUI.popup(f'Você perdeu! Pontuação: {score}')
                    pygame.quit()
                i += 1
        except IndexError as ie:
            pass

    UP = 0
    RIGHT = 1 
    DOWN = 2
    LEFT = 3

    pygame.init() # iniciar o jogo
    screen = pygame.display.set_mode((600, 600)) # tamanho da tela
    pygame.display.set_caption('Snake') # título do jogo
    icon = pygame.image.load('images/snakeIcon.png') # icone do jogo
    pygame.display.set_icon(icon) # colocar icone

    snake = [(500, 200), (520, 200), (540, 200)] # 3 blocos = corpo da cobra
    snake_skin = pygame.Surface((20, 20)) # sprite da cobra
    snake_skin.fill((50, 255, 50)) # aparência da cobra

    apple_pos = on_grid_random()
    apple = pygame.Surface((20, 20)) # sprite da maçã
    apple.fill((255, 50, 50)) # aparência da maçã

    score = 0
    my_direction = LEFT

    clock = pygame.time.Clock()

    speed = 15

    while True:
        clock.tick(speed)
        for event in pygame.event.get():
            
            # reconhecendo as setas e direções
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    if my_direction != DOWN:
                        my_direction = UP
                if event.key == K_DOWN or event.key == K_s:
                    if my_direction != UP:
                        my_direction = DOWN
                if event.key == K_LEFT or event.key == K_a: 
                    if my_direction != RIGHT:
                        my_direction = LEFT
                if event.key == K_RIGHT or event.key == K_d:
                    if my_direction != LEFT:
                        my_direction = RIGHT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))
            score += 1
            speed += 0.5

        for i in range(len(snake) -1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
            if apple_pos == snake[i]:
                apple_pos = on_grid_random()
                

        # movimentação da cobra
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 20)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 20)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 20, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 20, snake[0][1])

        screen.fill((25, 25, 25)) # cor do fundo
        screen.blit(apple, apple_pos) # nascimento da maçã

        # colisão consigo mesmo
        collision_in_yourself()

        # sair do jogo
        if event.type == QUIT:
            pygame.quit()
            PySimpleGUI.popup(f'Você saiu! Pontuação: {score}')

        for (x, y) in snake:
            screen.blit(snake_skin, (x, y)) # nascimento da cobra
            if x == 600 or x == -20 or y == 600 or y == -20: # caso encoste nas bordas, perde o jogo
                PySimpleGUI.popup(f'Você perdeu! Pontuação: {score}')
                pygame.quit()

        pygame.display.update()

main()