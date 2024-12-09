import pygame

from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.font = pygame.font.SysFont('Arial', 26)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius /1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return[a, b, c]

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2 )

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0 :
            self.cooldown(dt)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]: 
            if self.timer <= 0:
                self.shoot()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position, self.position)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def cooldown(self, dt):
       self.timer -= dt

    def draw_score(self, screen, score):
        white = (255, 255, 255)
        score_text = self.font.render(f"Your score: {score}", True, white)
        score_rect = score_text.get_rect(center = (SCREEN_WIDTH // 2, 20))
        screen.blit(score_text, score_rect)

    def draw_lives(self, screen, lives):

        white = (255, 255, 255)
        for i in range(lives):
            x = 450 + i * (TRIANGLE_SIZE + TRIANGLE_SPACING)
            y = 10
            points = [(x, y), (x - TRIANGLE_SIZE // 2, y + TRIANGLE_SIZE), (x + TRIANGLE_SIZE // 2, y + TRIANGLE_SIZE)]
            pygame.draw.polygon(screen, white, points)




    
