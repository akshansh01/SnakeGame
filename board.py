import pygame as py

game_width = 800
game_height = 600
rect_vector = {py.K_LEFT: (-5, 0), py.K_RIGHT: (5, 0), py.K_UP: (0, -5), py.K_DOWN: (0, 5)}
rect_velocity = {py.K_LEFT: False, py.K_RIGHT: False, py.K_UP: False, py.K_DOWN: False}

x = 200
y = 200
snake_width = 20
snake_height = 20


def check_collision(snake_head):
    if snake_head.centerx + 10 > game_width:
        return True
    if snake_head.centerx - 10 < 0:
        return True
    if snake_head.centery - 10 < 0:
        return True
    if snake_head.centery + 10 > game_height:
        return True


def reset_velocity():
    for key in rect_velocity:
        rect_velocity[key] = False
