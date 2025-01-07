import os
import pygame
import sys

import hud
from hud import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class StartScreen:

    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.options = ["Play", "Scores", "Exit"]  # Opcje menu
        self.selected_option = 0  # Index aktualnie wybranej opcji
        self.name = Hud()

    def display(self):
        pygame.font.init()  # Initialize fonts in Pygame

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        font_title = pygame.font.SysFont('Arial', 40)  # Set font
        font = pygame.font.SysFont('Arial', 25)

        running = True

        while running:
            screen.fill((0, 0, 0))

            title = font_title.render('Asteroids the Game', True, (255, 255, 255))
            screen.blit(title, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 10))

            # Menu with arrow pointer
            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected_option else (150, 150, 150)
                text = font.render(option, True, color)
                x = SCREEN_WIDTH / 4
                y = SCREEN_HEIGHT / 4.5 + i * 40
                screen.blit(text, (x, y))

                # add arrow pointer
                if i == self.selected_option:
                    arrow = font.render("->", True, (255, 255, 255))
                    screen.blit(arrow, (x - 30, y))

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit program if user closes the window

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # arrow down
                        self.selected_option = (self.selected_option + 1) % len(self.options)

                    elif event.key == pygame.K_UP:  # arrow up
                        self.selected_option = (self.selected_option - 1) % len(self.options)

                    elif event.key == pygame.K_RETURN:  # Enter

                        if self.selected_option == 0:
                            return
                        elif self.selected_option == 1:
                            print("Scores selected!")

                        elif self.selected_option == 2:
                            print("Exit selected!")
                            pygame.quit()
                            sys.exit()

            pygame.display.flip()
            clock.tick(30)

