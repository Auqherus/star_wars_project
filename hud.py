import sys
import pygame
from constants import TRIANGLE_SIZE, TRIANGLE_SPACING, BEST_SCORE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_STATUS_STOP


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


def screen_settings():

    current_width, current_height = pygame.display.get_window_size()
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 45)
    pause_text = font.render("Paused", True, white)
    game_over_text = font.render("Game Over", True, white)
    pause_rect = pause_text.get_rect(center=(current_width / 2, current_height / 2))
    return pause_text, pause_rect, current_width, current_height, clock, font, game_over_text


class Hud:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.options = ["main menu", "exit"]
        self.selected_option = 0

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

    def pause_game(self, screen):

        pause_text, pause_rect, current_width, current_height, clock, font, game_over_text = screen_settings()
        screen.blit(pause_text, pause_rect)
        paused = True

        while paused:
            
            self.screen.fill((1, 1, 1))

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
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       paused = False
                    if event.key == pygame.K_DOWN:  # arrow down
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_UP:  # arrow up
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:  # Enter
                        if self.selected_option == 0:
                            print("GAME_STATUS_STOP == True")
                            paused = False
                            return True
                        elif self.selected_option == 1:
                            pygame.quit()
                            sys.exit()
            
            screen.blit(pause_text, pause_rect)
            pygame.display.flip()
            clock.tick(15)

    def death_screen(self):
        pause_text, pause_rect, current_width, current_height, clock, font, game_over_text = screen_settings()
        blink_interval = 500
        last_toggle_time = pygame.time.get_ticks()
        show_text = True
        game_over = False

        while not game_over:
            self.screen.fill((1, 1, 1))  # screen clearance

            # Time update
            current_time = pygame.time.get_ticks()

            # Blinking of text
            if current_time - last_toggle_time >= blink_interval:
                show_text = not show_text
                last_toggle_time = current_time

            if show_text:
                self.screen.blit(game_over_text, pause_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        return

            pygame.display.flip()
            clock.tick(60)

    def get_player_name(self):
        pygame.font.init()  # Initialize fonts in Pygame
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
            self.screen.fill((1, 1, 1))  # black
            txt_surface = font.render(text, True, color)  # Render the text

            # Set the width of the input box to fit the text
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw the text
            pygame.draw.rect(self.screen, color, input_box, 2)  # Draw the rectangle around the input box

            prompt = font.render('Enter your name:', True, (255, 255, 255))
            self.screen.blit(prompt, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4))  # Draw prompt on the screen

            if error_message:  # If there's an error, display it
                error_msg = font.render(error_message, True, (255, 0, 0))
                self.screen.blit(error_msg, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8))  # Draw error message


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

            clock.tick(15)

        return text  # Return the entered name
