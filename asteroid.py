from circleshape import CircleShape
import pygame
import random
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.astroid_variables.ASTEROID_COLOR, self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.astroid_variables.ASTEROID_MIN_RADIUS:
            return
        else:
            splitting_angle = random.uniform(20, 50)
            angle1 = self.velocity.rotate(splitting_angle)
            angle2 = self.velocity.rotate(-splitting_angle)
            new_radius = self.radius - constants.astroid_variables.ASTEROID_MIN_RADIUS
            new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid1.velocity = angle1 * 1.2
            new_astroid2.velocity = angle2 * 1.2

