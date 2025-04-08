import random

import pygame as pg

pg.init()
SIZE = WIDTH, HEIGHT = 1920, 1080
FPS = 120
BACKGROUND_COLOR = '#FF8C24'
INVERSE_EVENT = pg.USEREVENT + 1
INVERSE_EVENT_INTERVAL = 10 * 1000


class Amir:
    MIN_HEIGHT = 10
    MAX_HEIGHT = 200
    TEXT = 'Джигит'
    COLOR = 'black'
    SPEED_SIZE = 20
    SPEED = 1000
    MAX_SPEED_ROTATE = 150

    def __init__(self):
        self.x = random.randrange(1, WIDTH - Amir.MIN_HEIGHT * 10)
        self.y = random.randrange(1, HEIGHT - Amir.MIN_HEIGHT)
        self.speed_x = self.SPEED * random.choice((-1, 1))
        self.speed_y = self.SPEED * random.choice((-1, 1))
        self.size = random.randint(Amir.MIN_HEIGHT, Amir.MAX_HEIGHT)
        self.size_change = random.choice((-1, 1))
        self.rect = pg.Rect(0, 0, 0, 0)
        self.rotate_angle = 0
        self.rotate_speed = random.randint(-Amir.MAX_SPEED_ROTATE, Amir.MAX_SPEED_ROTATE)

    def draw(self, screen: pg.Surface):
        font = pg.font.SysFont('Arial', round(self.size))
        img = font.render(self.TEXT, True, self.COLOR)
        img = pg.transform.rotate(img, self.rotate_angle)
        self.rect = img.get_rect().move(self.x, self.y)

        screen.blit(img, (self.x, self.y))

    def update(self):
        if self.size >= Amir.MAX_HEIGHT:
            self.size_change = -1
        elif self.size <= Amir.MIN_HEIGHT:
            self.size_change = 1
        self.size += self.size_change * Amir.SPEED_SIZE / FPS
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
            self.y += self.speed_y / FPS
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
            self.x += self.speed_x / FPS
        self.x += self.speed_x / FPS
        self.y += self.speed_y / FPS
        self.rotate_angle += self.rotate_speed / FPS


screen = pg.display.set_mode(SIZE)
amirs = [Amir() for _ in range(10)]
clock = pg.time.Clock()
running = True
pg.time.set_timer(INVERSE_EVENT, INVERSE_EVENT_INTERVAL)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == INVERSE_EVENT:
            BACKGROUND_COLOR, Amir.COLOR = Amir.COLOR, BACKGROUND_COLOR
    screen.fill(BACKGROUND_COLOR)
    for amir in amirs:
        amir.update()
        amir.draw(screen)
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
