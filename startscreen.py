import os
import sys
import pygame
from hud import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class StartScreen:

    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.options = ["Play", "Scores", "Exit"]  # Options of the menu
        self.selected_option = 0  # Index of current chosen option
        self.name = Hud()

    def display(self):
        pygame.font.init()  # Initialize fonts in Pygame

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        font_title = pygame.font.SysFont('Arial', 40)  # Set font for the title
        font = pygame.font.SysFont('Arial', 25)  # Set font for the menu options

        running = True

        while running:
            screen.fill((1, 1, 1))

            # Get current window size
            current_width, current_height = pygame.display.get_window_size()

            # Render the title dynamically
            title = font_title.render('Asteroids the Game', True, (255, 255, 255))
            title_rect = title.get_rect(center=(current_width / 2, current_height / 5))
            screen.blit(title, title_rect.topleft)

            # Render the menu options dynamically
            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected_option else (150, 150, 150)
                text = font.render(option, True, color)
                text_rect = text.get_rect(center=(current_width / 2, current_height / 2.5 + i * 40))
                screen.blit(text, text_rect.topleft)

                # Render the arrow pointer dynamically
                if i == self.selected_option:
                    arrow = font.render("->", True, (255, 255, 255))
                    arrow_rect = arrow.get_rect(center=(text_rect.left - 20, text_rect.centery))
                    screen.blit(arrow, arrow_rect.topleft)

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
