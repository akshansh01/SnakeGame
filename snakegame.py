import pygame as py

py.init()

game_display = py.display.set_mode((800, 600))
py.display.set_caption("Snake")

clock = py.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x = 200
y = 200
width = 100
height = 50

blue_rect = py.Rect(x, y, width, height)

rect_vector = {py.K_LEFT: (-5, 0), py.K_RIGHT: (5, 0), py.K_UP: (0, -5), py.K_DOWN: (0,5)}
key_holds = {py.K_LEFT: False, py.K_RIGHT: False, py.K_UP: False, py.K_DOWN: False}

game_loop = True
# Game Loop, don't put anything below this line.
while game_loop:
    game_display.fill(WHITE)
    for event in py.event.get():
        if event.type == py.QUIT:
            game_loop = False
        if event.type == py.KEYDOWN and event.key in [py.K_UP, py.K_DOWN, py.K_RIGHT, py.K_LEFT]:
            key_holds[event.key] = True
        if event.type == py.KEYUP and event.key in [py.K_UP, py.K_DOWN, py.K_RIGHT, py.K_LEFT]:
            key_holds[event.key] = False

    for key, value in key_holds.items():
        if value:
            blue_rect.move_ip(rect_vector[key])

    py.draw.rect(game_display, BLUE, blue_rect)
    py.display.flip()
    clock.tick(60)

py.quit()
