import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    dt = 0
    score = 0
    lives = 3

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()

    #asteroidsfield = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_enemy = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_enemy, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)

    player = Player(x, y)
    #asteroids_enemy = Asteroid(x, y, ASTEROID_MAX_RADIUS) #not nessesary here, can be deleted
    asteroidsfield = AsteroidField()
    
    

    while True: # game loop, working until interrupted

        for updates in updatable:
            updates.update(dt)

        
        for enemy in asteroids_enemy:
            for bullet in shot:
                if bullet.check_collision(enemy):
                    bullet.kill()
                    enemy.split()
                    score += 1
            if enemy.check_collision(player):
                print("Game over!")
                return
            
        screen.fill((1, 1, 1))

        for draws in drawable:
            draws.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.draw_score(screen, score)
        player.draw_lives(screen, lives)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
