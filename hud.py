import os
import pygame
import sys
from constants import *
from player import *
from circleshape import *


def draw_lives(screen, lives):

    white = (255, 255, 255)
    for i in range(lives):
        x = 450 + i * (TRIANGLE_SIZE + TRIANGLE_SPACING)
        y = 10
        points = [(x, y), (x - TRIANGLE_SIZE // 2, y + TRIANGLE_SIZE), (x + TRIANGLE_SIZE // 2, y + TRIANGLE_SIZE)]
        pygame.draw.polygon(screen, white, points)


def load_best_scores():
    try:
        with open(BEST_SCORE, "r") as file:
            scores = []
            if not scores:
                for _ in range(5):
                    score = ("Player", 0)
                    scores.append(score)
            for line in file:
                if ": " in line:
                    name, score = line.split(": ")
                    scores.append((name, int(score.strip())))
            return sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    except FileNotFoundError:
        return [("Player", 0), ("Player", 0), ("Player", 0), ("Player", 0), ("Player", 0)]


def save_best_score(name, score):
    scores = load_best_scores()
    scores.append((name, score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    with open(BEST_SCORE, 'w') as file:
        for name, score in scores:
            file.write(f"{name}: {score}\n")


class Hud:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)

    def draw_score(self, screen, score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Your score: {score}", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 30))
        screen.blit(score_text, score_rect)

    def draw_best_score(self, screen, best_player_name,  best_score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Best player: {best_player_name} : {best_score} ", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 10))
        screen.blit(score_text, score_rect)

    def draw_top_scores(self, screen, top_scores):
        white = (255, 255, 255)
        y_offset = 10
        for i, (name, score) in enumerate(top_scores):
            score_text = self.font.render(f"{i + 1}. {name}: {score}", True, white)
            screen.blit(score_text, (10, y_offset))
            y_offset += 25

    def get_player_name(self):
        pygame.font.init()  # Initialize fonts in Pygame

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        clock = pygame.time.Clock()

        font = pygame.font.SysFont('Arial', 30)  # Set font
        input_box = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, SCREEN_WIDTH / 2, 40)  # Rectangle for text input
        color_inactive = pygame.Color('lightskyblue3')  # Text color when the input box is inactive
        color_active = pygame.Color('dodgerblue2')  # Text color when the input box is active
        color = color_inactive
        active = False  # Initially, the input box is not active
        text = ''  # Initial text
        error_message = ""  # To store the error message

        running = True
        while running:
            screen.fill((0, 0, 0)) # black
            txt_surface = font.render(text, True, color)  # Render the text

            # Set the width of the input box to fit the text
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw the text
            pygame.draw.rect(screen, color, input_box, 2)  # Draw the rectangle around the input box

            prompt = font.render('Enter your name:', True, (255, 255, 255))
            screen.blit(prompt, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))  # Draw prompt on the screen

            if error_message:  # If there's an error, display it
                error_msg = font.render(error_message, True, (255, 0, 0))
                screen.blit(error_msg, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8))  # Draw error message

            pygame.display.flip()  # Update the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit program if user closes the window
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):  # Check if the input box was clicked
                        active = True
                        color = color_active
                    else:
                        active = False
                        color = color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:  # Submit the name when Enter is pressed
                            if text.strip() == "": 
                                error_message = "Error: Name cannot be empty!"
                            elif not text.isalpha():  
                                error_message = "Error: Only letters are allowed!"
                            else:
                                return text  # Valid input, return name
                        elif event.key == pygame.K_BACKSPACE:  # Delete a character if Backspace is pressed
                            text = text[:-1]
                            error_message = ""  # Clear the error message
                        else:
                            text += event.unicode  # Add new character to the text

            clock.tick(30)  

        return text  # Return the entered name


