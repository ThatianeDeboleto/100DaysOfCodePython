import pygame

def initialize_pygame():
    pygame.init()

def draw_enemies(enemy_list, screen, enemy_pos, enemy_size, PINK):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, PINK, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_screen():
    pygame.display.update()

def draw_player(screen, RED, player_pos, player_size):
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

def set_fps(clock):
    clock.tick(30)

def print_score(score, myFont,  YELLOW, screen, WIDTH, HEIGHT):
    text = "Score: " + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))

def fill_background(screen, BACKGROUND_COLOUR):
    screen.fill(BACKGROUND_COLOUR)