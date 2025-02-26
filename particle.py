import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, color, lifetime = 0.5):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        self.lifetime = max(lifetime, 0)

    def update(self, dt):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        self.lifetime = max(self.lifetime - dt, 0)
        if self.lifetime <= 0:
            self.kill()