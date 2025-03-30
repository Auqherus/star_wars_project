from shot import *
from particle import  *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.font = pygame.font.SysFont('Arial', 26)
        self.invincible = False
        self.invincible_timer = 0
        self.visible = True

    # draw player
    def triangle(self): 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.visible:
            white = (255, 255, 255)
            pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        if self.invincible:
            self.invincible_timer -= dt
            if self.invincible_timer <= 0:
                self.invincible = False
                self.visible = True  # Player stop blinking
            else:
                # Blinking per 0.2 sec
                self.visible = int(self.invincible_timer * 10) % 2 == 0

        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.cooldown(dt)

        #if not self.invincible:  # Player can't move while respawning
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

    def explode(self, particles_group):
        """Explosive effect and reset of a position of player"""
        white = (255, 255, 255)
        for _ in range(20):  # Particles
            particles_group.add(Particle(self.position, color=white))
        self.reset_position()

    def reset_position(self):
        """Reset player position and makes him invisible."""
        self.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.invincible = True
        self.invincible_timer = 3
        self.visible = True
