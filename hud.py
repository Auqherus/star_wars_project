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

class Hud:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 26)

    def draw_score(self, screen, score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Your score: {score}", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 20))
        screen.blit(score_text, score_rect)

