import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()

    asteroidsfield = pygame.sprite.Group()
    asteroids_enemy = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_enemy, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(x, y)
    #asteroids_enemy = Asteroid(x, y, ASTEROID_MAX_RADIUS) #not nessesary here, can be deleted
    asteroidsfield = AsteroidField()
    
    

    while True:

        for updates in updatable:
            updates.update(dt)
        
        for object in asteroids_enemy:
            if object.check_collision(player) == True:
                print("Game over!")
                return

        screen.fill((1, 1, 1))

        for draws in drawable:
            draws.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
