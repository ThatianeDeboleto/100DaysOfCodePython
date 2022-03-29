import pygame
import random
import sys

import model as m
import view as v

v.initialize_pygame()

def game_loop():
    #declare width and height of screen
    WIDTH = 800
    HEIGHT = 600

    #rgb codes of various colours
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BACKGROUND_COLOUR = (0, 0, 0) #black

    #player variables
    player_size = 50
    player_pos = [WIDTH/2, HEIGHT-2*player_size]

    #enemy variables
    enemy_size = 50
    enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
    enemy_list = [enemy_pos]

    SPEED = 10

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    score = 0

    clock = pygame.time.Clock()

    myFont = pygame.font.SysFont("monospace", 35)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT and m.not_overflow_left(player_pos, player_size, WIDTH):
                    x -= player_size
                elif event.key == pygame.K_RIGHT and m.not_overflow_right(player_pos, player_size, WIDTH):
                    x += player_size

                player_pos = [x, y]
        
        v.fill_background(screen, BACKGROUND_COLOUR)
        
        enemy_list = m.drop_enemies(enemy_list, WIDTH, enemy_size)
        enemy_list, score = m.update_enemy_positions(enemy_list, score, SPEED, HEIGHT)
        SPEED = m.set_level(score, SPEED)
        
        v.print_score(score, myFont, YELLOW, screen, WIDTH, HEIGHT)

        game_over = m.collision_check(enemy_list, player_pos, player_size, enemy_size)
        
        v.draw_enemies(enemy_list, screen, enemy_pos, enemy_size, BLUE)

        v.draw_player(screen, RED, player_pos, player_size)

        v.set_fps(clock)

        v.update_screen()

if __name__ == '__main__':
    game_loop()