from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import *
from startscreen import *
import os
import pygame

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
def game_loop():

    dt = 0
    top_scores = load_best_scores()
    best_player_name, best_score = top_scores[0] if top_scores else ("No Player", 0)

    score = 0
    lives = 3

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_enemy = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    hud = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    mainmenu = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_enemy, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)
    Hud.containers = (hud, updatable, drawable)
    StartScreen.containers = (mainmenu, updatable, drawable)

    player = Player(x, y)
    mainmenu = StartScreen()
    hud = Hud()
    mainscreen = mainmenu.display()
    start_screen = StartScreen()


    player_name = hud.get_player_name()  # Get player name from Hud
    asteroidsfield = AsteroidField()
    is_game_running = True

    while is_game_running:
        for updates in updatable:
            updates.update(dt)
            top_scores = load_best_scores()



        for enemy in asteroids_enemy:
            for bullet in shot:
                if bullet.check_collision(enemy):
                    bullet.kill()
                    enemy.split(particles)
                    score += 1

                    if score > best_score:
                        best_score = score
                        best_player_name = player_name

            if enemy.check_collision(player) and not player.invincible:
                enemy.kill()
                lives -= 1
                player.explode(particles)

                if lives == 0:
                    if score > top_scores[-1][1] if top_scores else 0:
                        save_best_score(player_name, score)
                    hud.death_screen()
                    print("Game over!")
                    return

        screen.fill((1, 1, 1))

        for draws in drawable:
            draws.draw(screen)

        hud.draw_score(screen, score)
        hud.draw_best_score(screen, best_player_name, best_score)
        hud.draw_top_scores(screen, top_scores)

        draw_lives(screen, lives)

        particles.update(dt)
        particles.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if hud.pause_game(screen):
                        return  #esc to main menu

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    while True:
        game_loop()

if __name__ == "__main__":
    main()



