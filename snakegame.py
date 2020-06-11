import pygame as py
import board as board
import random as random

py.init()

game_display = py.display.set_mode((board.game_width, board.game_height))
py.display.set_caption("Snake")

clock = py.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

snake_body = []
snake_block = py.Rect(board.x, board.y, board.snake_width, board.snake_height)
snake_head = snake_block.copy()
snake_body.append(py.Rect(board.x - 5, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 10, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 15, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 20, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 25, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 30, board.y, board.snake_width, board.snake_height))
snake_body.append(py.Rect(board.x - 35, board.y, board.snake_width, board.snake_height))

game_loop = True
# Game Loop, don't put anything below this line.
while game_loop:
    game_display.fill(BLACK)
    for event in py.event.get():
        if event.type == py.QUIT:
            game_loop = False
        if event.type == py.KEYDOWN and event.key in [py.K_UP, py.K_DOWN, py.K_RIGHT, py.K_LEFT]:
            board.reset_velocity()
            board.rect_velocity[event.key] = True

    for key, value in board.rect_velocity.items():
        if value:
            prev = snake_head.copy()
            snake_head.move_ip(board.rect_vector[key])
            for block in snake_body:
                prev2 = block.copy()
                block.move_ip(prev.x-block.x, prev.y-block.y)
                prev = prev2

    if board.check_collision(snake_head):
        board.reset_velocity()
    py.draw.rect(game_display, WHITE, snake_head)
    for block in snake_body:
        py.draw.rect(game_display, WHITE, block)
    py.display.update()
    clock.tick(60)

py.quit()
