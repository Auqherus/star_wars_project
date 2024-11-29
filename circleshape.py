import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, circle):
        pass

    def update(self, dt):
        pass

    def check_collision(self, object):
        distance = pygame.math.Vector2.distance_to(self.position, object.position)
        r_sum = self.radius + object.radius

        return distance <= r_sum