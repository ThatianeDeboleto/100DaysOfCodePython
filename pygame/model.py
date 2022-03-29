import random

def set_level(score, SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 11
    elif score < 80:
        SPEED = 14
    elif score < 100:
        SPEED = 17
    else:
        SPEED = 20
    #SPEED = score/5 + 5
    return SPEED

def drop_enemies(enemy_list, WIDTH, enemy_size):
    delay = random.random()
    if len(enemy_list) < 11 and delay < 0.08:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
    return enemy_list

def update_enemy_positions(enemy_list, score, SPEED, HEIGHT):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return enemy_list, score

def collision_check(enemy_list, player_pos, player_size, enemy_size):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos, player_size, enemy_size):
            return True
    return False

def detect_collision(player_pos, enemy_pos, player_size, enemy_size):
    p_x = player_pos[0]
    p_y= player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def not_overflow_left(player_pos, player_size, WIDTH):
    if 0 < player_pos[0]:
        return True
    return False

def not_overflow_right(player_pos, player_size, WIDTH):
    if player_pos[0] + player_size < WIDTH:
        return True
    return False