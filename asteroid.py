from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, circle):
        pygame.draw.circle(self.screen, (self.x, self.y), self.radius, 2)

    def update(self, dt):
        self.velocity += (self.velocity * dt)

    