import os
import sys
import pygame

import hud
from hud import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from main import game_loop


class StartScreen:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.options = ["Play", "Scores", "Exit"]
        self.selected_option = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def show_scores(self):
        """Showing best scores on the screen -- > Scores."""
        top_scores = load_best_scores()
        font = pygame.font.SysFont('Arial', 25)
        running = True
        r_pressed_time = None  # Variable that counts how long is 'R' pressed

        while running:
            self.screen.fill((0, 0, 0))  # Black screen
            title = font.render("Top Scores", True, (255, 255, 255))
            self.screen.blit(title, (SCREEN_WIDTH // 2 - 50, 50))

            # Drawing scores
            y_offset = 100
            for i, (name, score) in enumerate(top_scores):
                score_text = font.render(f"{i + 1}. {name}: {score}", True, (255, 255, 255))
                self.screen.blit(score_text, (SCREEN_WIDTH // 3, y_offset))
                y_offset += 40

            back_text = font.render("Press ESC to go back", True, (200, 200, 200))
            self.screen.blit(back_text, (SCREEN_WIDTH // 3, y_offset + 20))

            # For reset scores
            reset_text = font.render("Hold 'R' for 3s to reset scores", True, (200, 50, 50))
            self.screen.blit(reset_text, (SCREEN_WIDTH // 3, y_offset + 60))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Back to main menu
                    elif event.key == pygame.K_r:
                        r_pressed_time = pygame.time.get_ticks()  # Save time of pressed 'R'
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        r_pressed_time = None  # Reset if 'R' was pressed shorter than 3 sec

            # Check if 'R' is pressed 3 sec
            if r_pressed_time and pygame.time.get_ticks() - r_pressed_time >= 3000:
                # Reset Scores
                with open(BEST_SCORE, "w") as file:
                    file.write("")
                #top_scores = [("Player", 0) for _ in range(5)]  # Update local scores
                top_scores = load_best_scores()
                r_pressed_time = None  # Reset of time, which 'R' was pressed

    def display(self):
        pygame.font.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        font_title = pygame.font.SysFont('Arial', 40)
        font = pygame.font.SysFont('Arial', 25)

        running = True

        while running:
            screen.fill((1, 1, 1))

            title = font_title.render('Asteroids the Game', True, (255, 255, 255))
            title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5))
            screen.blit(title, title_rect.topleft)

            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i == self.selected_option else (150, 150, 150)
                text = font.render(option, True, color)
                text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.5 + i * 40))
                screen.blit(text, text_rect.topleft)

                if i == self.selected_option:
                    arrow = font.render("->", True, (255, 255, 255))
                    arrow_rect = arrow.get_rect(center=(text_rect.left - 20, text_rect.centery))
                    screen.blit(arrow, arrow_rect.topleft)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                            return  # Start the game
                        elif self.selected_option == 1:
                            self.show_scores()  # Shows the best scores
                        elif self.selected_option == 2:
                            pygame.quit()
                            sys.exit()

            pygame.display.flip()
            clock.tick(30)

