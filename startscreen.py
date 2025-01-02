import os
import pygame
import sys
from constants import *

class StartScreen:
    
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)

    def display(self):
        pygame.font.init()  # Initialize fonts in Pygame

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        clock = pygame.time.Clock()
        font_title = pygame.font.SysFont('Arial', 40)  # Set font
        font = pygame.font.SysFont('Arial', 25)

        running = True

        while running:
            screen.fill((0, 0, 0))

            tittle = font_title.render('Asteroids the Game', True, (255, 255, 255))
            play = font.render('Play', True, (255, 255, 255))
            info = font.render('Scores', True, (255, 255, 255))
            exit = font.render('Exit', True, (255, 255, 255))

            screen.blit(tittle, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 10)) 
            screen.blit(play, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4.5))
            screen.blit(info, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 3.5))
            screen.blit(exit, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2.9))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit program if user closes the window


            pygame.display.flip()  # Update the screen

            clock.tick(30)
    


