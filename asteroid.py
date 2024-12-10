from circleshape import *
from constants import *
from particle import Particle
import math
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.asteroid_shape = self.generate_asteroid(x, y, radius, random.randint(6, 12))

    def generate_asteroid(self, center_x, center_y, radius, num_points):
        points = []
        angle_step = 360 / num_points

        for i in range(num_points):
            angle = math.radians(i * angle_step)
            random_radius = radius * random.uniform(0.7, 1.3) # random radius for asteroids different shapes
            x = center_x + random_radius * math.cos(angle)
            y = center_y + random_radius * math.sin(angle)
            points.append((x, y))

        return points

    def draw(self, screen):
        white = (255, 255, 255)
        #pygame.draw.circle(screen, white, self.position, self.radius, 2) # unnecessary , can be deleted
        pygame.draw.polygon(screen, white, self.asteroid_shape, width=1)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.asteroid_shape = [(x + self.velocity.x * dt, y + self.velocity.y * dt) for x, y in self.asteroid_shape]

    def split(self, particle_group):
        white = (255, 255, 255)
        self.kill()

        for _ in range(10):
            particle = Particle(self.position, white)
            particle_group.add(particle)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           angle = random.uniform(20, 50)
           a_1 = Asteroid(self.position.x, self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
           a_2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
           a_1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
           a_2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2

