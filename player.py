from circleshape import CircleShape
import pygame
import constants
from Shot import Shot

class Player(CircleShape):
    Score:int = 0
    def __init__(self, x, y):
        super().__init__(x, y, constants.player_variables.PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, constants.player_variables.PLAYER_COLOR, self.triangle(), constants.player_variables.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants.player_variables.PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.player_variables.PLAYER_SPEED * dt

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.player_variables.PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(0-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = constants.player_variables.PLAYER_SHOOT_COOLDOWN

    def is_colliding(self, CircleShape):
        for point in self.triangle():
            if CircleShape.radius >= point.distance_to(CircleShape.position):
                return True
        return False
    
