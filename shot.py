from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, lifetime=4.0):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = lifetime  # Lifetime of the bullet
        self.timer = 0  # Initialisation of the timer
        self.velocity = pygame.Vector2(0, -1)  # Direction of the bullet on start

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, self.position, self.radius, 2) # Draw a bullet - to change bullet radius, check constants
        

    def update(self, dt):
        self.timer += dt  # Lifetime update
        if self.timer > self.lifetime:
            self.kill()  # If lifetime passed, delete bullet

        # Bullet moving
        self.position += self.velocity * dt
