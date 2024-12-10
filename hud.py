import os

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


def load_best_score():
    if os.path.exists(BEST_SCORE):
        with open(BEST_SCORE, 'r') as f:
            try:
                return int(f.read(). strip())
            except ValueError:
                return 0
    return 0

def save_best_score(score):
    with open(BEST_SCORE, 'w') as file:
        file.write(str(score))


class Hud:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 20)

    def draw_score(self, screen, score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Your score: {score}", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 30))
        screen.blit(score_text, score_rect)

    def draw_best_score(self, screen, best_score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Your best score: {best_score}", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 10))
        screen.blit(score_text, score_rect)

