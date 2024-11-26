import pygame
from constants import *
from player import *

def main():
    pygame.init()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()

    while True:

        screen.fill((1, 1, 1))
        player.update(dt)
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
