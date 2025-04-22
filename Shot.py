import pygame
from circleshape import CircleShape
import constants
import importlib

class Shot(CircleShape):
    def __init__(self, x, y):
        importlib.reload(constants)
        super().__init__(x, y, constants.shooting_contsants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.shooting_contsants.SHOT_COLOR, self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt