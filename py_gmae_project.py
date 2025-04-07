import pygame as pg

SIZE = WIDHT, HEIGHT = 800, 400
COLOR_SKY = pg.Color(255, 125, 0)
COLOR_GROUND = pg.Color(0, 120, 0)
COLOR_SUN = 'yellow'
SUN_RADIOS = 50


def darkness(color: pg.Color, light: float) -> pg.Color:
    h, s, l, a = color.hsla
    light = max(0, light)
    new_color = pg.Color(color)
    new_color.hsla = (h, s, int(l * light), a)
    return new_color


pg.init()
screen = pg.display.set_mode(SIZE)
ruunning = True
animation = 0

while ruunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if animation < 1:
        animation += 0.001

    screen.fill(darkness(COLOR_SKY, 1 - animation))
    sun_y = HEIGHT / 2 + SUN_RADIOS * animation
    pg.draw.circle(screen, COLOR_SUN, (WIDHT / 2, sun_y), SUN_RADIOS)

    pg.draw.rect(screen, darkness(COLOR_GROUND, 1 - animation), (0, HEIGHT / 2, WIDHT, HEIGHT / 2))
    pg.display.flip()
