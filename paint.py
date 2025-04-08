import pygame as pg

pg.init()

SIZE = WIDTH, HEIGHT = 1920, 1024
RADIOS = 10
COLOR_BLACK = 'black'
COLOR_BLUE = 'blue'
COLOR_RED = 'red'
BACKGROUND = 'white'

colors = [COLOR_BLACK, COLOR_BLUE, COLOR_RED]
current_color_index = 0

screen = pg.display.set_mode(SIZE)
screen.fill(BACKGROUND)
pg.display.flip()

running = True
drawing = False

while running:
    event = pg.event.wait()

    if event.type == pg.QUIT:
        running = False

    elif event.type == pg.MOUSEBUTTONDOWN:
        if event.button == pg.BUTTON_LEFT:
            drawing = True

    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == pg.BUTTON_LEFT:
            drawing = False

    elif event.type == pg.MOUSEMOTION and drawing:
        pg.draw.circle(screen, colors[current_color_index], event.pos, RADIOS)
        pg.display.flip()

    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_RETURN:
            screen.fill(BACKGROUND)
        elif event.key == pg.K_r:  # Если нажата клавиша 'R'
            current_color_index = (current_color_index + 1) % len(colors)  # Переключаем цвет

    pg.display.flip()

pg.quit()