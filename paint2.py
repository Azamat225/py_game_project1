import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Имя 'Азамат' (не игра)")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_A(x, y):
    pygame.draw.line(screen, RED, (x, y), (x + 50, y - 100), 5)
    pygame.draw.line(screen, RED, (x + 50, y - 100), (x + 100, y), 5)
    pygame.draw.line(screen, RED, (x + 25, y - 50), (x + 75, y - 50), 5)

def draw_Z(x, y):
    pygame.draw.line(screen, RED, (x, y), (x + 100, y), 5)
    pygame.draw.line(screen, RED, (x, y), (x + 100, y - 100), 5)
    pygame.draw.line(screen, RED, (x, y - 100), (x + 100, y - 100), 5)

def draw_M(x, y):
    pygame.draw.line(screen, RED, (x, y), (x, y - 100), 5)
    pygame.draw.line(screen, RED, (x, y - 100), (x + 50, y - 50), 5)
    pygame.draw.line(screen, RED, (x + 50, y - 50), (x + 100, y - 100), 5)
    pygame.draw.line(screen, RED, (x + 100, y - 100), (x + 100, y), 5)

def draw_T(x, y):
    pygame.draw.line(screen, RED, (x, y - 100), (x + 100, y - 100), 5)
    pygame.draw.line(screen, RED, (x + 50, y - 100), (x + 50, y), 5)

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_A(50, 300)
        draw_Z(150, 300)
        draw_A(250, 300)
        draw_M(350, 300)
        draw_A(450, 300)
        draw_T(550, 300)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()